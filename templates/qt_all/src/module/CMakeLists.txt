cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

add_library({{module.name}} {{module.name}} {{module.name}}.cpp)
target_include_directories({{module.name}}
    PUBLIC 
        $<INSTALL_INTERFACE:..>    
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/..>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/..
)

{% if module.depends %}
target_link_libraries({{module.name}} PUBLIC {{" ".join(module.depends)}})
{% endif %}

