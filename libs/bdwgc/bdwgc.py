# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.CMakePackageBase import CMakePackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["8.2.10"]:
            self.targets[ver] = f"https://github.com/ivmai/bdwgc/releases/download/v{ver}/gc-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"gc-{ver}"
        self.targetDigests["8.2.10"] = (["832cf4f7cf676b59582ed3b1bbd90a8d0e0ddbc3b11cb3b2096c5177ce39cc47"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Boehm-Demers-Weiser conservative garbage collector"
        self.webpage = "https://www.hboehm.info/gc/"
        self.defaultTarget = "8.2.10"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += ["-Denable_docs=OFF"]
