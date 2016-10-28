.. _additional_arguments:

Additional Arguments
====================

You will likely need to pass additional variables to your commands in order for
them to run properly.  An example would be a config object with all of your
config options.  This is accomplished by passing additional arguments to the
HelCLI object when instantiated.

In practice it looks like this:

.. code-block:: python

    from helcli import HelCLI


    var_one = "test1"
    var_two = "test2"
    cli = HelCLI(sub_commands='command_dir',
                 description='A simple CLI',
                 var_one, var_two)
    cli.run()

Then when it comes time to use this variable in the ``main`` function of all our
commands these are available as an additional variable.

.. code-block:: python

    def main(parser_d, additional_args):
        # unpack additional_args
        var_one, var_two = additional_args
        print(var_one)  # prints "test1"
        print(var_two)  # prints "test2"

.. note::
    If you pass additional arguments to the HelCLI object you will need to
    have the ``additional_args`` variable passed in the ``main()`` function in
    *all* of your commands, or else you will get errors.
