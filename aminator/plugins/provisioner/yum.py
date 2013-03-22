# -*- coding: utf-8 -*-

#
#
#  Copyright 2013 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#

"""
aminator.plugins.provisioner.yum
================================
basic yum provisioner
"""
import logging

from aminator.plugins.provisioner.linux import BaseLinuxProvisionerPlugin
from aminator.util.linux import yum_clean_metadata, yum_install, rpm_package_metadata

__all__ = ('YumProvisionerPlugin',)
log = logging.getLogger(__name__)


class YumProvisionerPlugin(BaseLinuxProvisionerPlugin):
    """
    YumProvisionerPlugin takes the majority of its behavior from BaseLinuxProvisionerPlugin
    See BaseLinuxProvisionerPlugin for details
    """
    _name = 'yum'

    def _refresh_package_metadata(self):
        return yum_clean_metadata()

    def _provision_package(self):
        context = self._config.context
        return yum_install(context.package.arg)

    def _store_package_metadata(self):
        context = self._config.context
        metadata = rpm_package_metadata(context.package.arg)
        context.package.name = metadata.get('name', context.package.arg)
        context.package.version = metadata.get('version', '_')
        context.package.release = metadata.get('release', '_')
