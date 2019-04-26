
from conans import ConanFile, CMake


class QtAll(ConanFile):
    name = "qt_all"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"

    exports_sources = "src/*", "CMakeLists.txt"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["qtbase", "qtsvg", "qtdeclarative", "qtactiveqt", "qtscript", "qtmultimedia", "qttools", "qtxmlpatterns", "qttranslations", "qtdoc", "qtrepotools", "qtqa", "qtlocation", "qtsensors", "qtconnectivity", "qtwayland", "qt3d", "qtimageformats", "qtgraphicaleffects", "qtquickcontrols", "qtserialbus", "qtserialport", "qtx11extras", "qtmacextras", "qtwinextras", "qtandroidextras", "qtwebsockets", "qtwebchannel", "qtwebengine", "qtcanvas3d", "qtwebview", "qtquickcontrols2", "qtpurchasing", "qtcharts", "qtdatavis3d", "qtvirtualkeyboard", "qtgamepad", "qtscxml", "qtspeech", "qtnetworkauth", "qtremoteobjects", "qtwebglplugin"]