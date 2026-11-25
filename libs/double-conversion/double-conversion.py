# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.CMakePackageBase import CMakePackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["3.3.1"]:
            self.targets[ver] = f"https://github.com/google/double-conversion/archive/refs/tags/v{ver}.tar.gz"
            self.targetInstSrc[ver] = f"double-conversion-{ver}"
        self.targetDigests["3.3.1"] = (["fe54901055c71302dcdc5c3ccbe265a6c191978f3761ce1414d0895d6b0ea90e"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Efficient binary-decimal and decimal-binary conversion routines for IEEE doubles"
        self.webpage = "https://github.com/google/double-conversion"
        self.defaultTarget = "3.3.1"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
