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

from helcli.config import get_config
from helcli.parser import get_parser, gen_parser
import importlib
import inspect


class HelCLI(object):
    def __init__(self, sub_commands, description=None, config_files=None):
        """
        :param description: A description of your CLI
        :type description: str
        :param sub_commands: Location of sub-command folder
        :type sub_commands: str
        :param config_files: Where to read config files from
        :type config_files: list(str)
        """
        self._sub_commands = sub_commands
        self._config = get_config(config_files)
        self._parser, self._subparser = get_parser(description)

    def run(self):
        """ Runs CLI, provided information passed in class initialization """
        caller = self._caller_module()
        gen_parser(caller, self._sub_commands, self._parser, self._subparser)
        parser_dict = vars(self._parser.parse_args())
        self._run_command(caller, self._sub_commands, parser_dict['command'],
                          parser_dict, self._config)

    @staticmethod
    def _caller_module():
        """
        :returns: Calling module of this module
        :rtype: string
        """
        # < 3.3 implementation is cosidered a hack for inspecting the frame
        stack = inspect.stack()
        # [2] who calls this guys caller
        parentframe = stack[2][0]
        module = inspect.getmodule(parentframe)
        # Handle if a submodule of a module is calling
        if "." in module.__name__:
            return module.__name__.split('.')[0]
        return module.__name__  # A base module is calling

    @staticmethod
    def _run_command(caller, commands, command, parser, config):
        """
        Run the main function in given command module
        :param caller: Module calling this module
        :type caller: string
        :param commands: Sub-module relative to caller with commands
        :type commands: string
        :param command: The command sub-module to run
        :type command: string
        :param parser: Dictionary of Argparse object
        :type parser: dict
        :param config: A configparser object with CLI config
        :type config: configparser.ConfigParser
        """
        command_module = importlib.import_module(
            '{}.{}.{}'.format(caller, commands, command))
        command_module.main(parser, config)

# vim:et:fdm=marker:sts=4:sw=4:ts=4
