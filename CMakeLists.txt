cmake_minimum_required(VERSION 3.16)
project(azure-pipeline-cpp)
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_SOURCE_DIR}/build/modules)
find_package(spdlog CONFIG REQUIRED)

add_executable(demo src/main.cpp)
target_link_libraries(demo PUBLIC spdlog::spdlog)
target_compile_features(demo PUBLIC cxx_std_20)
install(TARGETS demo DESTINATION .)
