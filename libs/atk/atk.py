# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["2.38.0"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/atk/{majorMinor}/atk-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"atk-{ver}"
        self.targetDigests["2.38.0"] = (["ac4de2a4ef4bd5665052952fe169657e65e895c5057dffb3c2a810f6191a0c36"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Accessibility toolkit (needed by GTK 3)"
        self.webpage = "https://gitlab.gnome.org/GNOME/atk"
        self.defaultTarget = "2.38.0"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/glib"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += ["-Dintrospection=false"]
