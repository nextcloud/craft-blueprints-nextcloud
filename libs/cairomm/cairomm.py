# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["1.14.5"]:
            self.targets[ver] = f"https://www.cairographics.org/releases/cairomm-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"cairomm-{ver}"
        self.targetDigests["1.14.5"] = (["70136203540c884e89ce1c9edfb6369b9953937f6cd596d97c78c9758a5d48db"], CraftHash.HashAlgorithm.SHA256)

        self.description = "C++ bindings for cairo (cairomm-1.0 API)"
        self.webpage = "https://www.cairographics.org/cairomm/"
        self.defaultTarget = "1.14.5"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/cairo"] = None
        self.runtimeDependencies["libs/libsigcpp"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += ["-Dbuild-examples=false", "-Dbuild-tests=false"]
