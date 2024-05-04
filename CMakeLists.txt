# Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# policies up to CMake 3.27
cmake_minimum_required(VERSION 3.15...3.27)

# Scikit-build-core sets these values for you, or you can just hard-code the
# name and version.
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

# Find the module development requirements (requires FindPython from 3.17 or
# scikit-build-core's built-in backport)
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

# Add C++ libraries
#add_library(astar SHARED src/astar.cpp)

# 
pybind11_add_module(graph src/graph.cpp src/astar.cpp)
#target_link_libraries(graph PRIVATE astar)
# Link against your C++ libraries
#target_link_libraries(mymodule PRIVATE libA libB)

# This is passing in the version as a define just as an example
target_compile_definitions(graph PRIVATE VERSION_INFO=${PROJECT_VERSION})

# The install directory is the output (wheel) directory
install(TARGETS graph DESTINATION path_planning)
