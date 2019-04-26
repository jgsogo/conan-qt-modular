cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library(qttranslations qttranslations.h qttranslations.cpp)
target_include_directories(qttranslations
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)


target_link_libraries(qttranslations PUBLIC qttools)

