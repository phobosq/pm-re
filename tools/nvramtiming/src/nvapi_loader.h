#pragma once

#include <cstdint>
#include <string>
#include <vector>

namespace nvramtiming {

using NvStatus = std::int32_t;
using NvPhysicalGpuHandle = void*;

constexpr NvStatus kNvApiOk = 0;
constexpr std::uint32_t kNvApiInitializeId = 0x0150E828u;
constexpr std::uint32_t kNvApiUnloadId = 0xD22BDD7Eu;
constexpr std::uint32_t kNvApiEnumPhysicalGpusId = 0xE5AC921Fu;
constexpr std::uint32_t kNvApiGpuGetFullNameId = 0xCEEE8E9Fu;
constexpr std::uint32_t kNvApiGpuGetPciIdentifiersId = 0x2DDFB66Eu;
constexpr std::uint32_t kNvApiGpuRegisterOpId = 0x2EB3C140u;
constexpr std::uint32_t kNvApiMaxPhysicalGpus = 64;
constexpr std::uint32_t kNvApiShortStringMax = 64;

struct GpuInfo {
  std::uint32_t index{};
  NvPhysicalGpuHandle handle{};
  std::string name;
};

struct PciIdentifiers {
  std::uint32_t device_id{};
  std::uint32_t subsystem_id{};
  std::uint32_t revision_id{};
  std::uint32_t ext_device_id{};
};

class NvApi {
 public:
  NvApi() = default;
  NvApi(const NvApi&) = delete;
  NvApi& operator=(const NvApi&) = delete;
  ~NvApi();

  bool load(std::string& error);
  std::vector<GpuInfo> enumerate(std::string& error) const;
  bool get_pci_identifiers(NvPhysicalGpuHandle gpu, PciIdentifiers& ids,
                           std::string& error) const;
  bool read_register(NvPhysicalGpuHandle gpu, std::uint32_t reg,
                     std::uint64_t& value, std::string& error) const;
  bool write_register_masked(NvPhysicalGpuHandle gpu, std::uint32_t reg,
                             std::uint64_t mask, std::uint64_t value,
                             std::string& error) const;
  bool register_op_available() const noexcept { return register_op_ != nullptr; }

 private:
  void reset() noexcept;

  void* module_{};
  void* query_interface_{};
  void* initialize_{};
  void* unload_{};
  void* enum_physical_gpus_{};
  void* gpu_get_full_name_{};
  void* gpu_get_pci_identifiers_{};
  void* register_op_{};
  bool initialized_{};
};

}  // namespace nvramtiming
