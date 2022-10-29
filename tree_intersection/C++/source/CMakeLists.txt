set(BINARY ${CMAKE_PROJECT_NAME})

file(GLOB_RECURSE SOURCES LIST_DIRECTORIES true *.h *.hpp *.cpp)

set(SOURCES ${SOURCES})

add_executable(${BINARY}_run ${SOURCES})

add_library(${BINARY}_lib SHARED ${SOURCES})

target_link_libraries(${BINARY}_lib PRIVATE nlohmann_json::nlohmann_json)
target_link_libraries(${BINARY}_run PRIVATE nlohmann_json::nlohmann_json)
target_link_libraries(${BINARY}_run PRIVATE ${BINARY}_lib)