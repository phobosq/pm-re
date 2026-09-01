#include "nvapi_loader.h"

#include <cerrno>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
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

struct VmrPlan {
  VmrFamily family{};
  nvramtiming::PciIdentifiers pci{};
  std::uint64_t original_raw{};
  std::uint32_t current_field{};
  std::uint32_t base_field{};
  std::uint32_t desired_field{};
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

bool make_vmr_plan(const nvramtiming::NvApi& nvapi,
                   const nvramtiming::GpuInfo& gpu,
                   std::uint32_t vmr,
                   VmrPlan& plan,
                   std::string& error) {
  plan = {};
  if (!nvapi.get_pci_identifiers(gpu.handle, plan.pci, error)) {
    return false;
  }
  if (!classify_vmr_family(plan.pci.device_id, plan.family)) {
    std::ostringstream os;
    os << "PCI device ID 0x" << std::hex << std::uppercase << plan.pci.device_id
       << std::dec << " is not present in PhoenixMiner 6.2c Pascal VMR family table";
    error = os.str();
    return false;
  }
  if (!nvapi.read_register(gpu.handle, kVramTimingRegister, plan.original_raw, error)) {
    return false;
  }
  plan.current_field = static_cast<std::uint32_t>((plan.original_raw & kVmrMask) >> kVmrShift);
  plan.base_field = plan.current_field != 0 ? plan.current_field : plan.family.fallback_base;
  if (plan.base_field < plan.family.target) {
    std::ostringstream os;
    os << "Current/base VMR field " << plan.base_field << " is below family target "
       << plan.family.target << "; refusing to extrapolate";
    error = os.str();
    return false;
  }
  plan.desired_field = phoenix_vmr_field(plan.base_field, plan.family.target, vmr);
  if (plan.desired_field > 0x1FFu) {
    error = "Calculated VMR field does not fit the confirmed 9-bit register field";
    return false;
  }
  return true;
}

void print_vmr_plan(const nvramtiming::GpuInfo& gpu, std::uint32_t vmr,
                    const VmrPlan& plan) {
  const std::uint64_t preview_raw = (plan.original_raw & ~kVmrMask) |
      (static_cast<std::uint64_t>(plan.desired_field) << kVmrShift);
  std::cout << "GPU: [" << gpu.index << "] " << gpu.name << '\n'
            << "PCI device key: 0x" << std::hex << std::uppercase << plan.pci.device_id << std::dec << '\n'
            << "Phoenix family: " << plan.family.id << " (" << plan.family.memory << ")\n"
            << "VMR: " << vmr << " / 100\n"
            << "current field: " << plan.current_field << '\n'
            << "base field: " << plan.base_field
            << (plan.current_field == 0 ? " (type-8 fallback)" : " (hardware)") << '\n'
            << "target field: " << plan.family.target << '\n'
            << "desired field: " << plan.desired_field << '\n'
            << "register 0x9A0290 current: 0x" << std::hex << std::uppercase << plan.original_raw << '\n'
            << "register 0x9A0290 preview: 0x" << preview_raw << std::dec << '\n';
}

std::uint32_t vmr_field(std::uint64_t raw) {
  return static_cast<std::uint32_t>((raw & kVmrMask) >> kVmrShift);
}

}  // namespace

int main(int argc, char** argv) {
  bool list = (argc == 1);
  bool read_reg = false;
  bool vmr_preview = false;
  bool vmr_test = false;
  bool confirm_write = false;
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
    } else if (arg == "--vmr-preview" || arg == "--vmr-test") {
      if (i + 2 >= argc || !parse_u32(argv[i + 1], gpu_index) || !parse_u32(argv[i + 2], vmr) || vmr > 100) {
        std::cerr << "Usage: nvramtiming " << arg << " <gpu-index> <0..100>\n";
        return 2;
      }
      vmr_preview = (arg == "--vmr-preview");
      vmr_test = (arg == "--vmr-test");
      i += 2;
    } else if (arg == "--confirm-write") {
      confirm_write = true;
    } else if (arg == "--help" || arg == "-h") {
      std::cout << "nvramtiming MVP (NVIDIA Pascal)\n"
                   "Usage:\n"
                   "  nvramtiming --list\n"
                   "  nvramtiming --read-reg <gpu-index> <register>\n"
                   "  nvramtiming --vmr-preview <gpu-index> <0..100>\n"
                   "  nvramtiming --vmr-test <gpu-index> <0..100> --confirm-write\n\n"
                   "--vmr-test writes only the confirmed VMR field, verifies it, then immediately\n"
                   "restores and verifies the original field. There is no persistent apply mode.\n";
      return 0;
    } else {
      std::cerr << "Unknown argument: " << arg << '\n';
      return 2;
    }
  }

  if (vmr_test && !confirm_write) {
    std::cerr << "--vmr-test performs a real timing-register write. Add --confirm-write explicitly.\n";
    return 2;
  }
  if (confirm_write && !vmr_test) {
    std::cerr << "--confirm-write is only valid with --vmr-test\n";
    return 2;
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

  if (read_reg || vmr_preview || vmr_test) {
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

  if (vmr_preview || vmr_test) {
    VmrPlan plan{};
    if (!make_vmr_plan(nvapi, gpus[gpu_index], vmr, plan, error)) {
      std::cerr << error << '\n';
      return 1;
    }
    if (vmr_preview) {
      std::cout << "VMR preview only - NO WRITE\n";
      print_vmr_plan(gpus[gpu_index], vmr, plan);
    }

    if (vmr_test) {
      std::cout << "VMR TRANSACTION TEST - WILL WRITE AND RESTORE\n";
      print_vmr_plan(gpus[gpu_index], vmr, plan);
      if (plan.desired_field == plan.current_field) {
        std::cout << "Desired field equals current field; no write needed. PASS (no-op).\n";
        return 0;
      }

      const std::uint64_t desired_bits = static_cast<std::uint64_t>(plan.desired_field) << kVmrShift;
      const std::uint64_t original_bits = static_cast<std::uint64_t>(plan.current_field) << kVmrShift;
      bool write_succeeded = false;
      bool apply_verified = false;
      bool restore_succeeded = false;
      bool restore_verified = false;
      std::uint64_t after_apply = 0;
      std::uint64_t after_restore = 0;

      if (!nvapi.write_register_masked(gpus[gpu_index].handle, kVramTimingRegister,
                                       kVmrMask, desired_bits, error)) {
        std::cerr << "Apply write failed: " << error << '\n';
      } else {
        write_succeeded = true;
        if (!nvapi.read_register(gpus[gpu_index].handle, kVramTimingRegister,
                                 after_apply, error)) {
          std::cerr << "Apply readback failed: " << error << '\n';
        } else {
          apply_verified = (vmr_field(after_apply) == plan.desired_field);
          std::cout << "apply readback field: " << vmr_field(after_apply)
                    << (apply_verified ? " (PASS)" : " (MISMATCH)") << '\n';
        }
      }

      // Best-effort restore is attempted regardless of apply/readback outcome.
      error.clear();
      if (!nvapi.write_register_masked(gpus[gpu_index].handle, kVramTimingRegister,
                                       kVmrMask, original_bits, error)) {
        std::cerr << "RESTORE WRITE FAILED: " << error << '\n';
      } else {
        restore_succeeded = true;
        if (!nvapi.read_register(gpus[gpu_index].handle, kVramTimingRegister,
                                 after_restore, error)) {
          std::cerr << "RESTORE READBACK FAILED: " << error << '\n';
        } else {
          restore_verified = (vmr_field(after_restore) == plan.current_field);
          std::cout << "restore readback field: " << vmr_field(after_restore)
                    << (restore_verified ? " (PASS)" : " (MISMATCH)") << '\n';
        }
      }

      if (!restore_succeeded || !restore_verified) {
        std::cerr << "CRITICAL: original VMR field was not verified restored. Driver/GPU reset is recommended.\n";
        return 3;
      }
      if (!write_succeeded || !apply_verified) {
        std::cerr << "VMR transaction did not verify, but original field was restored successfully.\n";
        return 1;
      }
      std::cout << "VMR transaction PASS: desired value verified, original value restored and verified.\n";
    }
  }

  return 0;
}
