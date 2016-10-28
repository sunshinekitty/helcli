.. _getting_started:

Getting Started
===============

This guide will walk you through setting up an example CLI project using HelCLI.

Project Layout
--------------
::

    project-src/
        project/
            __init__.py
            commands/
                __init__.py
                example-command.py
        setup.py

project/__init__.py
^^^^^^^^^^^^^^^^^^^

This is where most of core CLI code will go, we need to instantiate the Class
and run it inside of a function.  When we go to reference this with an entry
point in setup.py we'll need to remember the name we use.  We will call it with
the ``main`` function as an example.  Our entry point will then be
``project:main``.

.. code-block:: python

    from helcli import HelCLI


    def main():
        cli = HelCLI(sub_commands='commands', description='A simple CLI')
        cli.run()


Great! Now when project.main() is called it will execute our CLI.  Take note
that sub_commands is set to 'commands'  this is the directory relative to our
package (project) where our sub-commands for this CLI will go.

project/commands/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python requires this file to know that the commands directory is a submodule
that we can import from.  It's fine to leave this file blank, it just needs to
exist.

project/commands/example-command.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HelCLI will be looking for commands inside of the 'commands' directory which we
set above.  It will go through every file in this directory when the ``run``
method is called on the HelCLI object and execute ``setup``.  This is where you
should setup any command line arguments you expect for this command.  Inside of
the main method is what should happen if someone is actually calling this
command.  The arguments you requested above will be passed to ``main`` as a
dictionary you can reference.

For this example let's have example-command take one argument, name, and have
the command print out 'Hello ``name``!'.  Note that it uses the
`argparse module <https://docs.python.org/dev/library/argparse.html>`_ to set
this up.

.. code-block:: python

    def setup(parser, subparsers):
        parser_example_command = subparsers.add_parser(
            'example-command',
            help='Prints "Hello <name>!"')

        parser_example_command.add_argument(
            'name',
            help='The name to say hello to.')

    def main(parser_d):
        name = parser_d['name']  # retrieved from parser name argument
        print 'Hello {}!'.format(name)

setup.py
^^^^^^^^

Lastly is our setup file.  This syntax isn't specific to HelCLI, but is included
for completeness.

.. code-block:: python

    from setuptools import setup, find_packages


    setup(name='project',
          version=0.0.1,
          author='You',
          author_email='you@mail.com',
          packages=find_packages(),
          install_requires=['helcli'],
          entry_points={'console_scripts': [
              'project = project:main',
          ]})


Wrapping up
-----------
Now you may ``pip install -e ./project-src`` and run the ``project`` command to
have a fully functional CLI.
