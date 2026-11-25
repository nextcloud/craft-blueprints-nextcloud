# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["3.24.52"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/gtk/{majorMinor}/gtk-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"gtk-{ver}"
        self.targetDigests["3.24.52"] = (["80931fa472a77b9a164f6740e3c0b444fac6770054632d35a7ff9d679e5e7b9f"], CraftHash.HashAlgorithm.SHA256)

        self.description = "GTK 3 widget toolkit"
        self.webpage = "https://www.gtk.org/"
        self.defaultTarget = "3.24.52"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/glib"] = None
        # the quartz backend needs cairo built with quartz support
        self.runtimeDependencies["libs/cairo"] = None
        self.runtimeDependencies["libs/pango"] = None
        self.runtimeDependencies["libs/gdk-pixbuf"] = None
        self.runtimeDependencies["libs/atk"] = None
        self.runtimeDependencies["libs/libepoxy"] = None
        self.runtimeDependencies["data/hicolor-icon-theme"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += [
            "-Dintrospection=false",
            "-Ddemos=false",
            "-Dexamples=false",
            "-Dtests=false",
        ]
