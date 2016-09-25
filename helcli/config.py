# Copyright (c) 2016 Alex Edwards
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


def get_config(locations):
    """
    Given locations, provide ConfigParser object
    :param locations: Config locations
    :type locations: string or list
    :returns: ConfigParser object
    :rtype: configparser.ConfigParser
    """
    config = configparser.ConfigParser()
    config.read(locations)
    return config

# vim:et:fdm=marker:sts=4:sw=4:ts=4
