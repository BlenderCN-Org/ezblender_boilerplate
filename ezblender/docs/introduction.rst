Introduction
=====================================

This page describes what you need to do to get your own EZBlender-based addon up and running inside Blender.

=============
Prerequisites
=============

* Blender version 2.79
* Basic knowledge of the Python programming language
* Basic knowledge of Blender

=============
Installation
=============

1. Navigate to your blender addons folder: ``Blender/2.79/scripts/addons``

2. Clone/extract the `EZBlender repository <https://github.com/anonoh/ezblender_boilerplate/>`_ into the ``Blender/2.79/scripts/addons`` folder (so that it now contains the folder ezblender_boilerplate)

    2.1. Optional: rename the ``ezblender_boilerplate`` folder to the name of your own addon

    2.2. Optional: Navigate into ``ezblender_boilerplate`` and open the file ``__init__.py``, here you can change some basic addon fields: addon name, author and category right at the top.

3. Start Blender and open the addons settings window, search for ezblender (or your new name) and enable the addon

=========================
Making a simple operator
=========================

Navigate to your ezblender_boilerplate folder and open the file addon.py, this is the entry point for your addon.

It should currently look like this:

.. code-block:: python

    def init(registry):
        pass

To make the addon do something, we can use this function to registers an operator

.. code-block:: python

    def init(registry):
        registry.register_operator("ez.my_op","My Operator",lambda world: print("Hello world"))

If we reload the addon in blender (Bound to the F8 key by default), we can open the operator menu (Space) and search for "My Operator". Running it should print "Hello World" to the System Console ``Window->Toggle System Console``