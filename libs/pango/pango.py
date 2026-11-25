# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors

import info
from Package.MesonPackageBase import MesonPackageBase
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["1.58.2"]:
            majorMinor = ".".join(ver.split(".")[:2])
            self.targets[ver] = f"https://download.gnome.org/sources/pango/{majorMinor}/pango-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"pango-{ver}"
        self.targetDigests["1.58.2"] = (["342385b6ca3b7c73455d7c80a13b7dbe4489e00bc3bd4c5bd6ed4dce421e374a"], CraftHash.HashAlgorithm.SHA256)

        self.description = "Library for laying out and rendering of text"
        self.webpage = "https://www.gtk.org/"
        self.defaultTarget = "1.58.2"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["libs/glib"] = None
        self.runtimeDependencies["libs/cairo"] = None
        self.runtimeDependencies["libs/harfbuzz"] = None
        self.runtimeDependencies["libs/fribidi"] = None
        self.runtimeDependencies["libs/fontconfig"] = None
        self.runtimeDependencies["libs/freetype"] = None


class Package(MesonPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # fontconfig/freetype are needed for pangoft2 (required by Inkscape)
        self.subinfo.options.configure.args += [
            "-Dintrospection=disabled",
            "-Dbuild-testsuite=false",
            "-Dbuild-examples=false",
            "-Dfontconfig=enabled",
            "-Dfreetype=enabled",
        ]
