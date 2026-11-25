# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["2.66.10"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/glibmm/{majorMinor}/glibmm-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"glibmm-{ver}"
        self.targetDigests["2.66.10"] = (["2b61780203aed98e701d3ea57c8f353e7c8ada9706a79be782f6c5153dd035c0"], CraftHash.HashAlgorithm.SHA256)

        self.description = "C++ bindings for GLib (glibmm-2.4 API)"
        self.webpage = "https://gtkmm.gnome.org/"
        self.defaultTarget = "2.66.10"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/glib"] = None
        self.runtimeDependencies["libs/libsigcpp"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += ["-Dbuild-examples=false"]
