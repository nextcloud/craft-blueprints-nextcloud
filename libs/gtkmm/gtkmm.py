# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["3.24.11"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/gtkmm/{majorMinor}/gtkmm-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"gtkmm-{ver}"
        self.targetDigests["3.24.11"] = (["19e383c82d5dd89db275e00b82864e90414d4c3fb3d100b2f996bcc2338a4cc7"], CraftHash.HashAlgorithm.SHA256)

        self.description = "C++ bindings for GTK 3 (gtkmm-3.0 API)"
        self.webpage = "https://gtkmm.gnome.org/"
        self.defaultTarget = "3.24.11"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/gtk3"] = None
        self.runtimeDependencies["libs/glibmm"] = None
        self.runtimeDependencies["libs/cairomm"] = None
        self.runtimeDependencies["libs/pangomm"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # no atkmm: Inkscape does not use it
        self.subinfo.options.configure.args += ["-Dbuild-atkmm-api=false", "-Dbuild-demos=false", "-Dbuild-tests=false"]
