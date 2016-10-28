HelCLI documentation
====================

.. toctree::
   :maxdepth: 2
   :hidden:

   getting-started.rst
   additional-arguments.rst


HelCLI is an opinionated way to create and organize your command line programs,
and aims to help bootstrap the process and provide a foundation that works for
most use cases.

In the most simplest form, HelCLI requires three lines of code to have a
functional command line program.

.. code-block:: python

    from helcli import HelCLI

    cli = HelCLI(sub_commands='command_dir', description='A simple CLI')
    cli.run()

To see some examples of HelCLI in use see the
`example project <https://github.com/sunshinekitty/helcli-example>`_, or
`Getting Started <getting-started.html>`_.
