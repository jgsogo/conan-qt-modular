cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library(qt3d qt3d.h qt3d.cpp)
target_include_directories(qt3d
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)


target_link_libraries(qt3d PUBLIC qtbase)

