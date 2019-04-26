cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library(qtdatavis3d qtdatavis3d.h qtdatavis3d.cpp)
target_include_directories(qtdatavis3d
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)


target_link_libraries(qtdatavis3d PUBLIC qtbase)

