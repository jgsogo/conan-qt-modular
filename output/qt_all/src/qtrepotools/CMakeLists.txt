cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library(qtrepotools qtrepotools.h qtrepotools.cpp)
target_include_directories(qtrepotools
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)


