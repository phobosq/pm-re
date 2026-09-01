#include "nvapi_loader.h"

#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include <array>
#include <sstream>
#include <utility>

namespace nvramtiming {
namespace {

using QueryInterfaceFn = void*(__cdecl*)(std::uint32_t);
using InitializeFn = NvStatus(__cdecl*)();
using UnloadFn = NvStatus(__cdecl*)();
using EnumPhysicalGpusFn = NvStatus(__cdecl*)(NvPhysicalGpuHandle*, std::uint32_t*);
using GpuGetFullNameFn = NvStatus(__cdecl*)(NvPhysicalGpuHandle, char*);
using GpuRegisterOpFn = NvStatus(__cdecl*)(NvPhysicalGpuHandle, void*);

struct RegisterOpEntry {
  std::uint16_t opcode;
  std::uint16_t reserved;
  std::uint32_t reg;
  std::uint64_t mask;
  std::uint64_t value;
};
static_assert(sizeof(RegisterOpEntry) == 0x18, "RegisterOpEntry ABI mismatch");

struct RegisterOpRequest1 {
  std::uint32_t version;
  std::uint32_t count;
  RegisterOpEntry entry;
};
static_assert(sizeof(RegisterOpRequest1) == 0x20, "RegisterOpRequest ABI mismatch");

constexpr std::uint32_t kRegisterOpRequestVersion = 0x00011808u;
constexpr std::uint16_t kRegisterOpRead = 0x0015u;

std::string win32_error(const char* prefix) {
  std::ostringstream os;
  os << prefix << " (Win32 error " << GetLastError() << ')';
  return os.str();
}

}  // namespace

NvApi::~NvApi() { reset(); }

void NvApi::reset() noexcept {
  if (initialized_ && unload_ != nullptr) {
    reinterpret_cast<UnloadFn>(unload_)();
  }
  if (module_ != nullptr) {
    FreeLibrary(static_cast<HMODULE>(module_));
  }
  module_ = nullptr;
  query_interface_ = nullptr;
  initialize_ = nullptr;
  unload_ = nullptr;
  enum_physical_gpus_ = nullptr;
  gpu_get_full_name_ = nullptr;
  register_op_ = nullptr;
  initialized_ = false;
}

bool NvApi::load(std::string& error) {
  reset();
  error.clear();

  HMODULE module = LoadLibraryW(L"nvapi64.dll");
  if (module == nullptr) {
    error = win32_error("LoadLibraryW(nvapi64.dll) failed");
    return false;
  }
  module_ = module;

  auto query = reinterpret_cast<QueryInterfaceFn>(GetProcAddress(module, "nvapi_QueryInterface"));
  if (query == nullptr) {
    error = win32_error("GetProcAddress(nvapi_QueryInterface) failed");
    reset();
    return false;
  }
  query_interface_ = reinterpret_cast<void*>(query);

  initialize_ = query(kNvApiInitializeId);
  unload_ = query(kNvApiUnloadId);
  enum_physical_gpus_ = query(kNvApiEnumPhysicalGpusId);
  gpu_get_full_name_ = query(kNvApiGpuGetFullNameId);
  register_op_ = query(kNvApiGpuRegisterOpId);

  if (initialize_ == nullptr || enum_physical_gpus_ == nullptr || gpu_get_full_name_ == nullptr) {
    error = "Required NVAPI interfaces are unavailable";
    reset();
    return false;
  }

  const NvStatus status = reinterpret_cast<InitializeFn>(initialize_)();
  if (status != kNvApiOk) {
    std::ostringstream os;
    os << "NvAPI_Initialize failed with status " << status;
    error = os.str();
    reset();
    return false;
  }
  initialized_ = true;
  return true;
}

std::vector<GpuInfo> NvApi::enumerate(std::string& error) const {
  error.clear();
  std::array<NvPhysicalGpuHandle, kNvApiMaxPhysicalGpus> handles{};
  std::uint32_t count = 0;
  const NvStatus status = reinterpret_cast<EnumPhysicalGpusFn>(enum_physical_gpus_)(handles.data(), &count);
  if (status != kNvApiOk) {
    std::ostringstream os;
    os << "NvAPI_EnumPhysicalGPUs failed with status " << status;
    error = os.str();
    return {};
  }

  if (count > handles.size()) {
    error = "NvAPI returned an invalid GPU count";
    return {};
  }

  std::vector<GpuInfo> result;
  result.reserve(count);
  for (std::uint32_t i = 0; i < count; ++i) {
    std::array<char, kNvApiShortStringMax> name{};
    const NvStatus name_status = reinterpret_cast<GpuGetFullNameFn>(gpu_get_full_name_)(handles[i], name.data());
    GpuInfo info;
    info.index = i;
    info.handle = handles[i];
    info.name = (name_status == kNvApiOk) ? std::string{name.data()} : std::string{"<name unavailable>"};
    result.push_back(std::move(info));
  }
  return result;
}

bool NvApi::read_register(NvPhysicalGpuHandle gpu, std::uint32_t reg,
                          std::uint64_t& value, std::string& error) const {
  error.clear();
  value = 0;
  if (!initialized_) {
    error = "NVAPI is not initialized";
    return false;
  }
  if (gpu == nullptr) {
    error = "Invalid physical GPU handle";
    return false;
  }
  if (register_op_ == nullptr) {
    error = "NvAPI_GPU_RegisterOp (0x2EB3C140) is unavailable";
    return false;
  }

  RegisterOpRequest1 req{};
  req.version = kRegisterOpRequestVersion;
  req.count = 1;
  req.entry.opcode = kRegisterOpRead;
  req.entry.reg = reg;

  const NvStatus status = reinterpret_cast<GpuRegisterOpFn>(register_op_)(gpu, &req);
  if (status != kNvApiOk) {
    std::ostringstream os;
    os << "NvAPI_GPU_RegisterOp(read 0x" << std::hex << reg
       << ") failed with status " << std::dec << status;
    error = os.str();
    return false;
  }

  value = req.entry.value;
  return true;
}

}  // namespace nvramtiming
