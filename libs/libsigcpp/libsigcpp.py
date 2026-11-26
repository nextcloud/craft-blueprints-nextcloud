# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["2.12.1"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/libsigc++/{majorMinor}/libsigc++-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"libsigc++-{ver}"
        self.targetDigests["2.12.1"] = (["a9dbee323351d109b7aee074a9cb89ca3e7bcf8ad8edef1851f4cf359bd50843"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Typesafe callback framework for C++ (sigc++-2.0)"
        self.webpage = "https://libsigcplusplus.github.io/libsigcplusplus/"
        self.defaultTarget = "2.12.1"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += ["-Dbuild-examples=false", "-Dbuild-tests=false"]
