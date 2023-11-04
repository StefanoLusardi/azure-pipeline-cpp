list(APPEND CMAKE_PREFIX_PATH ${CMAKE_SOURCE_DIR}/build/modules)

# library
add_library(demo)
add_library(demo::demo ALIAS demo)
find_package(spdlog CONFIG REQUIRED)
set(TARGET_HEADERS include/demo/foo.hpp)
set(TARGET_SOURCES src/foo.cpp)

target_sources(demo PUBLIC ${TARGET_HEADERS} PRIVATE ${TARGET_SOURCES})
target_include_directories(demo PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/include> $<INSTALL_INTERFACE:CMAKE_INSTALL_INCLUDEDIR>)
target_compile_features(demo PUBLIC cxx_std_20)
target_link_libraries(demo PRIVATE spdlog::spdlog)
set_target_properties(demo PROPERTIES VERSION ${${PROJECT_NAME}_VERSION} SOVERSION ${${PROJECT_NAME}_VERSION_MAJOR})
set_target_properties(demo PROPERTIES PUBLIC_HEADER "${TARGET_HEADERS}")
install(TARGETS demo PUBLIC_HEADER DESTINATION include/demo)

# examples
add_executable(example examples/demo_example.cpp)
target_link_libraries(example PUBLIC demo::demo)
target_compile_features(example PUBLIC cxx_std_20)

# tests
# TODO

# bindings
find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(pydemo bindings/demo_python.cpp)
target_link_libraries(pydemo PRIVATE demo)
target_compile_definitions(pydemo PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
