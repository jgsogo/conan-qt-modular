from conans import ConanFile
import os

class {{module.name}}(ConanFile):
    name = "{{module.name.lower()}}"
    version = "{{version}}"
    settings = "os", "arch", "compiler", "build_type"

    build_requires = "qt_all/{{version}}@{{user}}/{{channel}}"
    keep_imports = True

    def imports(self):
        # Includes
        self.copy("*{{module.name}}*.h", src="", dst="")
        # Libs
        self.copy("*{{module.name}}*.a", src="", dst="")
        self.copy("*{{module.name}}*.lib", src="", dst="")

    def build(self):
        pass

    {% if module.depends -%}
    def requirements(self):
        {% for it in module.depends -%}
        self.requires("{{it}}/{{version}}@{{user}}/{{channel}}")
        {% endfor %}
    {% endif -%}

    def package(self):
        self.copy("*.h")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["{{module.name}}"]
