# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["2.46.5"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/pangomm/{majorMinor}/pangomm-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"pangomm-{ver}"
        self.targetDigests["2.46.5"] = (["38ca0b050b065de4e3da0c182df657437757063bbf0c4b6c9567ddba019b1d68"], CraftHash.HashAlgorithm.SHA256)

        self.description = "C++ bindings for Pango (pangomm-1.4 API)"
        self.webpage = "https://gtkmm.gnome.org/"
        self.defaultTarget = "2.46.5"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/pango"] = None
        self.runtimeDependencies["libs/glibmm"] = None
        self.runtimeDependencies["libs/cairomm"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
