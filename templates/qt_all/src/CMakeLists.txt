cmake_minimum_required(VERSION 2.8)
project(QtAll CXX)

{% for it in modules %}
add_subdirectory(it)
{% endfor %}
