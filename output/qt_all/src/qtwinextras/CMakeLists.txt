cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library(qtwinextras qtwinextras.h qtwinextras.cpp)
target_include_directories(qtwinextras
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)


target_link_libraries(qtwinextras PUBLIC qtbase)

