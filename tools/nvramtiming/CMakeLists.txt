cmake_minimum_required(VERSION 3.20)
project(nvramtiming LANGUAGES CXX)

if(NOT WIN32)
  message(FATAL_ERROR "nvramtiming MVP is Windows-only")
endif()

add_executable(nvramtiming
  src/main.cpp
  src/nvapi_loader.cpp
)

target_compile_features(nvramtiming PRIVATE cxx_std_17)
target_include_directories(nvramtiming PRIVATE src)
target_compile_definitions(nvramtiming PRIVATE WIN32_LEAN_AND_MEAN NOMINMAX)

if(MSVC)
  target_compile_options(nvramtiming PRIVATE /W4 /permissive-)
endif()
