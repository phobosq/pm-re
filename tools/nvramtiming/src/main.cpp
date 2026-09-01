#include "nvapi_loader.h"

#include <cerrno>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>

namespace {

constexpr std::uint32_t kVramTimingRegister = 0x009A0290u;
constexpr std::uint64_t kVmrMask = 0x000000000001FF00ull;
constexpr unsigned kVmrShift = 8;

bool parse_u32(const char* text, std::uint32_t& value) {
  errno = 0;
  char* end = nullptr;
  const unsigned long v = std::strtoul(text, &end, 0);
  if (errno != 0 || end == text || *end != '\0' || v > std::numeric_limits<std::uint32_t>::max()) {
    return false;
  }
  value = static_cast<std::uint32_t>(v);
  return true;
}

struct VmrFamily {
  int id;
  const char* memory;
  std::uint32_t fallback_base;
  std::uint32_t target;
};

bool classify_vmr_family(std::uint32_t pci_device_id, VmrFamily& out) {
  // PhoenixMiner 6.2c table at RVA 0x4BD620. Keys are packed
  // (PCI device ID << 16) | 0x10DE.
  switch (pci_device_id) {
    // family 1: Pascal GDDR5X
    case 0x1B0010DEu: case 0x1B0110DEu: case 0x1B0210DEu:
    case 0x1B0610DEu: case 0x1B0710DEu: case 0x1B8010DEu:
    case 0x1B8710DEu: case 0x1BC710DEu:
      out = {1, "GDDR5X", 152u, 120u};
      return true;

    // family 0: Pascal GDDR5
    case 0x1B8110DEu: case 0x1B8210DEu: case 0x1B8310DEu:
    case 0x1B8410DEu: case 0x1C0210DEu: case 0x1C0310DEu:
    case 0x1C0410DEu: case 0x1C0610DEu: case 0x1C0710DEu:
    case 0x1C0910DEu: case 0x1C8110DEu: case 0x1C8210DEu:
    case 0x1C8310DEu:
      out = {0, "GDDR5", 220u, 130u};
      return true;

    default:
      return false;
  }
}

std::uint32_t phoenix_vmr_field(std::uint32_t base, std::uint32_t target,
                                std::uint32_t vmr) {
  // Mirrors 0x1D8B2D..0x1D8B57:
  // trunc(base - (base - target) * vmr / 100.0)
  const double result = static_cast<double>(base) -
      static_cast<double>(base - target) * static_cast<double>(vmr) / 100.0;
  return static_cast<std::uint32_t>(result);  // positive values: trunc toward zero
}

}  // namespace

int main(int argc, char** argv) {
  bool list = (argc == 1);
  bool read_reg = false;
  bool vmr_preview = false;
  std::uint32_t gpu_index = 0;
  std::uint32_t reg = 0;
  std::uint32_t vmr = 0;

  for (int i = 1; i < argc; ++i) {
    const std::string arg = argv[i];
    if (arg == "--list") {
      list = true;
    } else if (arg == "--read-reg") {
      if (i + 2 >= argc || !parse_u32(argv[i + 1], gpu_index) || !parse_u32(argv[i + 2], reg)) {
        std::cerr << "Usage: nvramtiming --read-reg <gpu-index> <register>\n";
        return 2;
      }
      read_reg = true;
      i += 2;
    } else if (arg == "--vmr-preview") {
      if (i + 2 >= argc || !parse_u32(argv[i + 1], gpu_index) || !parse_u32(argv[i + 2], vmr) || vmr > 100) {
        std::cerr << "Usage: nvramtiming --vmr-preview <gpu-index> <0..100>\n";
        return 2;
      }
      vmr_preview = true;
      i += 2;
    } else if (arg == "--help" || arg == "-h") {
      std::cout << "nvramtiming MVP (NVIDIA-only)\n"
                   "Usage:\n"
                   "  nvramtiming --list\n"
                   "  nvramtiming --read-reg <gpu-index> <register>\n"
                   "  nvramtiming --vmr-preview <gpu-index> <0..100>\n\n"
                   "Examples:\n"
                   "  nvramtiming --read-reg 0 0x9A0290\n"
                   "  nvramtiming --vmr-preview 0 50\n\n"
                   "Current build is strictly read-only. VMR preview calculates but does not write.\n";
      return 0;
    } else {
      std::cerr << "Unknown argument: " << arg << '\n';
      return 2;
    }
  }

  nvramtiming::NvApi nvapi;
  std::string error;
  if (!nvapi.load(error)) {
    std::cerr << "NVAPI initialization failed: " << error << '\n';
    return 1;
  }

  auto gpus = nvapi.enumerate(error);
  if (!error.empty()) {
    std::cerr << error << '\n';
    return 1;
  }

  if (list) {
    std::cout << "NVIDIA GPUs: " << gpus.size() << '\n';
    for (const auto& gpu : gpus) {
      std::cout << "[" << gpu.index << "] " << gpu.name << '\n';
    }
    std::cout << "NvAPI_GPU_RegisterOp (0x2EB3C140): "
              << (nvapi.register_op_available() ? "available" : "not available") << '\n';
  }

  if (read_reg || vmr_preview) {
    if (gpu_index >= gpus.size()) {
      std::cerr << "GPU index out of range: " << gpu_index << '\n';
      return 2;
    }
  }

  if (read_reg) {
    std::uint64_t value = 0;
    if (!nvapi.read_register(gpus[gpu_index].handle, reg, value, error)) {
      std::cerr << error << '\n';
      return 1;
    }
    std::cout << "GPU[" << gpu_index << "] " << gpus[gpu_index].name
              << " reg 0x" << std::hex << std::uppercase << reg
              << " = 0x" << std::setw(16) << std::setfill('0') << value
              << std::dec << '\n';
  }

  if (vmr_preview) {
    nvramtiming::PciIdentifiers ids{};
    if (!nvapi.get_pci_identifiers(gpus[gpu_index].handle, ids, error)) {
      std::cerr << error << '\n';
      return 1;
    }

    VmrFamily family{};
    if (!classify_vmr_family(ids.device_id, family)) {
      std::cerr << "PCI device ID 0x" << std::hex << std::uppercase << ids.device_id
                << std::dec << " is not present in PhoenixMiner 6.2c Pascal VMR family table\n";
      return 1;
    }

    std::uint64_t raw = 0;
    if (!nvapi.read_register(gpus[gpu_index].handle, kVramTimingRegister, raw, error)) {
      std::cerr << error << '\n';
      return 1;
    }

    const std::uint32_t current = static_cast<std::uint32_t>((raw & kVmrMask) >> kVmrShift);
    const std::uint32_t base = current != 0 ? current : family.fallback_base;
    if (base < family.target) {
      std::cerr << "Current/base VMR field " << base << " is below family target "
                << family.target << "; refusing to extrapolate\n";
      return 1;
    }
    const std::uint32_t desired = phoenix_vmr_field(base, family.target, vmr);
    const std::uint64_t preview_raw = (raw & ~kVmrMask) |
        (static_cast<std::uint64_t>(desired) << kVmrShift);

    std::cout << "VMR preview only - NO WRITE\n"
              << "GPU: [" << gpu_index << "] " << gpus[gpu_index].name << '\n'
              << "PCI device key: 0x" << std::hex << std::uppercase << ids.device_id << std::dec << '\n'
              << "Phoenix family: " << family.id << " (" << family.memory << ")\n"
              << "VMR: " << vmr << " / 100\n"
              << "current field: " << current << '\n'
              << "base field: " << base << (current == 0 ? " (type-8 fallback)" : " (hardware)") << '\n'
              << "target field: " << family.target << '\n'
              << "desired field: " << desired << '\n'
              << "register 0x9A0290 current: 0x" << std::hex << std::uppercase << raw << '\n'
              << "register 0x9A0290 preview: 0x" << preview_raw << std::dec << '\n';
  }

  return 0;
}
