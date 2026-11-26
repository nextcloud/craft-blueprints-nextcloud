# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["2.44.8"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/gdk-pixbuf/{majorMinor}/gdk-pixbuf-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"gdk-pixbuf-{ver}"
        self.targetDigests["2.44.8"] = (["919f529512961a12e81cd4b4b466a48c3933469e7f9a310c6513cd4fb252ba3c"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Image loading library"
        self.webpage = "https://gitlab.gnome.org/GNOME/gdk-pixbuf"
        self.defaultTarget = "2.44.8"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/glib"] = None
        self.runtimeDependencies["libs/libpng"] = None
        self.runtimeDependencies["libs/libjpeg-turbo"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # built-in loaders: no loaders.cache to generate and relocate
        self.subinfo.options.configure.args += [
            "-Dglycin=disabled",
            "-Dtiff=disabled",
            "-Dbuiltin_loaders=all",
            "-Dintrospection=disabled",
            "-Dman=false",
            "-Dtests=false",
            "-Dinstalled_tests=false",
        ]
