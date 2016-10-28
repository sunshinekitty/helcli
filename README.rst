helcli
======

.. image:: https://img.shields.io/pypi/v/helcli.svg
  :target: https://pypi.python.org/pypi/helcli
  :alt: Latest Version
.. image:: https://travis-ci.org/sunshinekitty/helcli.svg?branch=master
  :target: https://travis-ci.org/sunshinekitty/helcli
  :alt: Build Status
.. image:: https://readthedocs.org/projects/helcli/badge/?version=latest
  :target: https://helcli.readthedocs.io/en/latest/
  :alt: Documentation

HelCLI is an opinionated way to create and organize your command line programs,
and aims to help bootstrap the process and provide a foundation that works for
most use cases.

In the most simplest form, HelCLI requires three lines of code to have a
functional command line program.

.. code-block:: python

    from helcli import HelCLI

    cli = HelCLI(sub_commands='command_dir', description='A simple CLI')
    cli.run()


*******
Install
*******

::

   pip install helcli


*************
Documentation
*************

To see some examples of HelCLI in use see the
`example project <https://github.com/sunshinekitty/helcli-example>`_, or the
`documentation <https://helcli.readthedocs.io/en/latest/>`_.
