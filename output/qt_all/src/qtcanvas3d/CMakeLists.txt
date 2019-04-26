cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library(qtcanvas3d qtcanvas3d.h qtcanvas3d.cpp)
target_include_directories(qtcanvas3d
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)


target_link_libraries(qtcanvas3d PUBLIC qtdeclarative)

