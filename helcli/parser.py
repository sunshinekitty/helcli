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

import argparse
import importlib
import pkgutil


def get_parser(description):
    """
    Returns argparse object with commands
    :param description: Description for Argparse
    :type description: string
    :returns: Argparse of object, and Subparser object
    :rtype: argparse.ArgumentParser, argparse._SubParsersAction
    """
    parser = argparse.ArgumentParser(description=description)
    subparsers = parser.add_subparsers(dest='command')
    return parser, subparsers


def gen_parser(caller, commands, parser, subparsers):
    """
    Run setup() for all submodules of sub_commands
    :param caller: Module calling this module
    :type caller: string
    :param commands: Sub-module relative to caller with commands
    :type commands: string
    :param parser: Argparse object
    :type parser: argparse.ArgumentParser
    :param subparsers: Subparsers object
    :type subparsers: argparse._SubParsersAction
    """
    importlib.import_module('{}.{}'.format(caller, commands))
    for importer, modname, ispkg in \
            pkgutil.iter_modules('{}.{}'.format(caller, commands)):
        found_module = importlib.import_module(
            '{}.{}.{}'.format(caller, commands, modname))
        found_module.setup(parser, subparsers)

# vim:et:fdm=marker:sts=4:sw=4:ts=4
