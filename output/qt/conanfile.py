from conans import ConanFile

class Qt(ConanFile):
    name = "qt"
    version = "0.1"

    # settings = "os", "arch", "compiler", "build_type"

    options = {
        "qtbase": [True, False],
        "qtsvg": [True, False],
        "qtdeclarative": [True, False],
        "qtactiveqt": [True, False],
        "qtscript": [True, False],
        "qtmultimedia": [True, False],
        "qttools": [True, False],
        "qtxmlpatterns": [True, False],
        "qttranslations": [True, False],
        "qtdoc": [True, False],
        "qtrepotools": [True, False],
        "qtqa": [True, False],
        "qtlocation": [True, False],
        "qtsensors": [True, False],
        "qtconnectivity": [True, False],
        "qtwayland": [True, False],
        "qt3d": [True, False],
        "qtimageformats": [True, False],
        "qtgraphicaleffects": [True, False],
        "qtquickcontrols": [True, False],
        "qtserialbus": [True, False],
        "qtserialport": [True, False],
        "qtx11extras": [True, False],
        "qtmacextras": [True, False],
        "qtwinextras": [True, False],
        "qtandroidextras": [True, False],
        "qtwebsockets": [True, False],
        "qtwebchannel": [True, False],
        "qtwebengine": [True, False],
        "qtcanvas3d": [True, False],
        "qtwebview": [True, False],
        "qtquickcontrols2": [True, False],
        "qtpurchasing": [True, False],
        "qtcharts": [True, False],
        "qtdatavis3d": [True, False],
        "qtvirtualkeyboard": [True, False],
        "qtgamepad": [True, False],
        "qtscxml": [True, False],
        "qtspeech": [True, False],
        "qtnetworkauth": [True, False],
        "qtremoteobjects": [True, False],
        "qtwebglplugin": [True, False],
        }
    default_options = {
        "qtbase": True,
            "qtsvg": False,
            "qtdeclarative": False,
            "qtactiveqt": False,
            "qtscript": False,
            "qtmultimedia": False,
            "qttools": False,
            "qtxmlpatterns": False,
            "qttranslations": False,
            "qtdoc": False,
            "qtrepotools": False,
            "qtqa": False,
            "qtlocation": False,
            "qtsensors": False,
            "qtconnectivity": False,
            "qtwayland": False,
            "qt3d": False,
            "qtimageformats": False,
            "qtgraphicaleffects": False,
            "qtquickcontrols": False,
            "qtserialbus": False,
            "qtserialport": False,
            "qtx11extras": False,
            "qtmacextras": False,
            "qtwinextras": False,
            "qtandroidextras": False,
            "qtwebsockets": False,
            "qtwebchannel": False,
            "qtwebengine": False,
            "qtcanvas3d": False,
            "qtwebview": False,
            "qtquickcontrols2": False,
            "qtpurchasing": False,
            "qtcharts": False,
            "qtdatavis3d": False,
            "qtvirtualkeyboard": False,
            "qtgamepad": False,
            "qtscxml": False,
            "qtspeech": False,
            "qtnetworkauth": False,
            "qtremoteobjects": False,
            "qtwebglplugin": False,
            }

    def requirements(self):
        if self.options.qtbase:
            self.requires("qtbase/0.1@issue/testing")
        if self.options.qtsvg:
            self.requires("qtsvg/0.1@issue/testing")
        if self.options.qtdeclarative:
            self.requires("qtdeclarative/0.1@issue/testing")
        if self.options.qtactiveqt:
            self.requires("qtactiveqt/0.1@issue/testing")
        if self.options.qtscript:
            self.requires("qtscript/0.1@issue/testing")
        if self.options.qtmultimedia:
            self.requires("qtmultimedia/0.1@issue/testing")
        if self.options.qttools:
            self.requires("qttools/0.1@issue/testing")
        if self.options.qtxmlpatterns:
            self.requires("qtxmlpatterns/0.1@issue/testing")
        if self.options.qttranslations:
            self.requires("qttranslations/0.1@issue/testing")
        if self.options.qtdoc:
            self.requires("qtdoc/0.1@issue/testing")
        if self.options.qtrepotools:
            self.requires("qtrepotools/0.1@issue/testing")
        if self.options.qtqa:
            self.requires("qtqa/0.1@issue/testing")
        if self.options.qtlocation:
            self.requires("qtlocation/0.1@issue/testing")
        if self.options.qtsensors:
            self.requires("qtsensors/0.1@issue/testing")
        if self.options.qtconnectivity:
            self.requires("qtconnectivity/0.1@issue/testing")
        if self.options.qtwayland:
            self.requires("qtwayland/0.1@issue/testing")
        if self.options.qt3d:
            self.requires("qt3d/0.1@issue/testing")
        if self.options.qtimageformats:
            self.requires("qtimageformats/0.1@issue/testing")
        if self.options.qtgraphicaleffects:
            self.requires("qtgraphicaleffects/0.1@issue/testing")
        if self.options.qtquickcontrols:
            self.requires("qtquickcontrols/0.1@issue/testing")
        if self.options.qtserialbus:
            self.requires("qtserialbus/0.1@issue/testing")
        if self.options.qtserialport:
            self.requires("qtserialport/0.1@issue/testing")
        if self.options.qtx11extras:
            self.requires("qtx11extras/0.1@issue/testing")
        if self.options.qtmacextras:
            self.requires("qtmacextras/0.1@issue/testing")
        if self.options.qtwinextras:
            self.requires("qtwinextras/0.1@issue/testing")
        if self.options.qtandroidextras:
            self.requires("qtandroidextras/0.1@issue/testing")
        if self.options.qtwebsockets:
            self.requires("qtwebsockets/0.1@issue/testing")
        if self.options.qtwebchannel:
            self.requires("qtwebchannel/0.1@issue/testing")
        if self.options.qtwebengine:
            self.requires("qtwebengine/0.1@issue/testing")
        if self.options.qtcanvas3d:
            self.requires("qtcanvas3d/0.1@issue/testing")
        if self.options.qtwebview:
            self.requires("qtwebview/0.1@issue/testing")
        if self.options.qtquickcontrols2:
            self.requires("qtquickcontrols2/0.1@issue/testing")
        if self.options.qtpurchasing:
            self.requires("qtpurchasing/0.1@issue/testing")
        if self.options.qtcharts:
            self.requires("qtcharts/0.1@issue/testing")
        if self.options.qtdatavis3d:
            self.requires("qtdatavis3d/0.1@issue/testing")
        if self.options.qtvirtualkeyboard:
            self.requires("qtvirtualkeyboard/0.1@issue/testing")
        if self.options.qtgamepad:
            self.requires("qtgamepad/0.1@issue/testing")
        if self.options.qtscxml:
            self.requires("qtscxml/0.1@issue/testing")
        if self.options.qtspeech:
            self.requires("qtspeech/0.1@issue/testing")
        if self.options.qtnetworkauth:
            self.requires("qtnetworkauth/0.1@issue/testing")
        if self.options.qtremoteobjects:
            self.requires("qtremoteobjects/0.1@issue/testing")
        if self.options.qtwebglplugin:
            self.requires("qtwebglplugin/0.1@issue/testing")
        

    def package_id(self):
        self.info.header_only()