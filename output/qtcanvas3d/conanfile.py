from conans import ConanFile
import os

class qtcanvas3d(ConanFile):
    name = "qtcanvas3d"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"

    build_requires = "qt_all/0.1@issue/testing"
    keep_imports = True

    def imports(self):
        # Includes
        self.copy("*qtcanvas3d*.h", src="", dst="")
        # Libs
        self.copy("*qtcanvas3d*.a", src="", dst="")
        self.copy("*qtcanvas3d*.lib", src="", dst="")

    def build(self):
        pass

    def requirements(self):
        self.requires("qtdeclarative/0.1@issue/testing")
        
    def package(self):
        self.copy("*.h")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["qtcanvas3d"]