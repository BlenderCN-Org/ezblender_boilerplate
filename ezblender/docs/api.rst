.. ezblender documentation master file, created by
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

API
=====================================

This page contains all the data structures available in EZBlender. For basic usage examples, please see the Examples section.

========
Registry
========

The registry is the first type you will see in EZBlender. An instance is sent to the ``init`` function in ``addon.py``. You use it to register operators and import/export windows.

.. code-block:: python

    def init(registry): # <-- That's a Registry
        pass

.. automodule:: ezblender.registry
	:members:


======
World
======

The "World" is the main type for interacting with the Blender environment through EZBlender. An instance is sent to all operators when executed.

.. code-block:: python

    def my_op(world): # <-- That's a World
        pass
    
    def init(registry):
        registry.register_operator("ez.my_op","My Op",my_op)

.. automodule:: ezblender.world
    :members:

======
Mesh
======

.. automodule:: ezblender.mesh
    :members:


========
Armature
========

.. automodule:: ezblender.armature
    :members:


========
Bone
========

.. automodule:: ezblender.bone
    :members:

========
Vector
========

.. automodule:: ezblender.vector
    :members:
