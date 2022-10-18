cmake_minimum_required(VERSION 3.10)
project(tree_intersection)

set(CMAKE_CXX_STANDARD 14)

include_directories(source)

add_subdirectory(source)
add_subdirectory(tests)
add_subdirectory(lib/googletest)
add_subdirectory(lib/nlohmann_json)