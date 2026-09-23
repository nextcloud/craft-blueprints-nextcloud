# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Nextcloud GmbH and Nextcloud contributors
# -*- coding: utf-8 -*-

import info
from CraftCore import CraftCore
from Package.CMakePackageBase import CMakePackageBase
from Utils import CraftHash

class subinfo(info.infoclass):
    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/nlohmann-json"] = None
        self.descriptions = "openvfs fuse driver"

    def setTargets(self):
        self.svnTargets["main"] = "[git]https://github.com/opencloud-eu/openvfs|main"
        self.svnTargets["2fdf61c"] = "[git]https://github.com/opencloud-eu/openvfs||2fdf61c8a7c1bb57d78b618ac17eaed12208db7d"

        self.description = "OpenVFS Virtual Files for Linux"
        self.displayName = "OpenVFS"
        self.webpage = "https://github.com/opencloud-eu/openvfs/"

        self.defaultTarget = "2fdf61c"


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
