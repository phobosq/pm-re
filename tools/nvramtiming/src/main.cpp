#include "nvapi_loader.h"

#include <cerrno>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>

namespace {

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

}  // namespace

int main(int argc, char** argv) {
  bool list = (argc == 1);
  bool read_reg = false;
  std::uint32_t gpu_index = 0;
  std::uint32_t reg = 0;

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
    } else if (arg == "--help" || arg == "-h") {
      std::cout << "nvramtiming MVP (NVIDIA-only)\n"
                   "Usage:\n"
                   "  nvramtiming --list\n"
                   "  nvramtiming --read-reg <gpu-index> <register>\n\n"
                   "Examples:\n"
                   "  nvramtiming --read-reg 0 0x9A0290\n\n"
                   "Current build is strictly read-only. No RegisterOp write opcode is exposed.\n";
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

  if (read_reg) {
    if (gpu_index >= gpus.size()) {
      std::cerr << "GPU index out of range: " << gpu_index << '\n';
      return 2;
    }
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

  return 0;
}
