# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from CraftCore import CraftCore
from Package.CMakePackageBase import CMakePackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def registerOptions(self):
        self.parent.package.categoryInfo.platforms = CraftCore.compiler.Platforms.MacOS

    def setTargets(self):
        for ver in ["1.4.4"]:
            self.targets[ver] = f"https://media.inkscape.org/dl/resources/file/inkscape-{ver}.tar.xz"
        self.targetInstSrc["1.4.4"] = "inkscape-1.4.4_2026-05-05_dcaf3e7d9e"
        self.targetDigests["1.4.4"] = (["bbce5753a1e08b871a5cf16c665eb060700aaab9a6a379dc63f4c4d9b3b8856e"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Vector graphics editor"
        self.displayName = "Inkscape"
        self.webpage = "https://inkscape.org"
        self.defaultTarget = "1.4.4"

    def setDependencies(self):
        self.buildDependencies["dev-utils/pkgconf"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/gtkmm"] = None
        self.runtimeDependencies["libs/boost"] = None
        self.runtimeDependencies["libs/bdwgc"] = None
        self.runtimeDependencies["libs/double-conversion"] = None
        self.runtimeDependencies["libs/gsl"] = None
        self.runtimeDependencies["libs/lcms2"] = None
        self.runtimeDependencies["libs/potrace"] = None
        self.runtimeDependencies["libs/libxslt"] = None
        self.runtimeDependencies["libs/libpng"] = None
        self.runtimeDependencies["libs/gettext"] = None


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += [
            "-DWITH_NLS=OFF",
            "-DWITH_OPENMP=OFF",
            "-DWITH_GNU_READLINE=OFF",
            "-DWITH_GSPELL=OFF",
            "-DWITH_GSOURCEVIEW=OFF",
            "-DENABLE_POPPLER=OFF",
            "-DENABLE_POPPLER_CAIRO=OFF",
            "-DWITH_IMAGE_MAGICK=OFF",
            "-DWITH_GRAPHICS_MAGICK=OFF",
            "-DWITH_LIBCDR=OFF",
            "-DWITH_LIBVISIO=OFF",
            "-DWITH_LIBWPG=OFF",
        ]
