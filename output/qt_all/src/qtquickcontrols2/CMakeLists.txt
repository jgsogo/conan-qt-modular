cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library(qtquickcontrols2 qtquickcontrols2.h qtquickcontrols2.cpp)
target_include_directories(qtquickcontrols2
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)


target_link_libraries(qtquickcontrols2 PUBLIC qtgraphicaleffects)

