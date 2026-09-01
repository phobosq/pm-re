#include "nvapi_loader.h"

#include <iostream>
#include <string>

int main(int argc, char** argv) {
  bool list = (argc == 1);
  for (int i = 1; i < argc; ++i) {
    const std::string arg = argv[i];
    if (arg == "--list") {
      list = true;
    } else if (arg == "--help" || arg == "-h") {
      std::cout << "nvramtiming MVP (NVIDIA-only)\n"
                   "Usage:\n"
                   "  nvramtiming --list\n\n"
                   "Current build is intentionally read-only. Register writes stay disabled\n"
                   "until the PhoenixMiner VMR -> register mapping and RegisterOp ABI are fully verified.\n";
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

  if (list) {
    auto gpus = nvapi.enumerate(error);
    if (!error.empty()) {
      std::cerr << error << '\n';
      return 1;
    }
    std::cout << "NVIDIA GPUs: " << gpus.size() << '\n';
    for (const auto& gpu : gpus) {
      std::cout << "[" << gpu.index << "] " << gpu.name << '\n';
    }
    std::cout << "NvAPI_GPU_RegisterOp (0x2EB3C140): "
              << (nvapi.register_op_available() ? "available" : "not available") << '\n';
  }

  return 0;
}
