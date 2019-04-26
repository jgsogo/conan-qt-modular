from conans import ConanFile
import os

class qtscxml(ConanFile):
    name = "qtscxml"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"

    build_requires = "qt_all/0.1@issue/testing"
    keep_imports = True

    def imports(self):
        # Includes
        self.copy("*qtscxml*.h", src="", dst="")
        # Libs
        self.copy("*qtscxml*.a", src="", dst="")
        self.copy("*qtscxml*.lib", src="", dst="")

    def build(self):
        pass

    def requirements(self):
        self.requires("qtbase/0.1@issue/testing")
        self.requires("qtdeclarative/0.1@issue/testing")
        
    def package(self):
        self.copy("*.h")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["qtscxml"]