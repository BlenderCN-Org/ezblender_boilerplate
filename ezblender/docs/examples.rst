.. ezblender documentation master file, created by
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Examples
=====================================

This page contains a few examples of ``addon.py`` for some common things you may want to do with EZBlender


=========================
Making a simple operator
=========================

Registers an operator that prints out "Hello World" when executed

.. code-block:: python

    def init(registry):
        registry.register_operator("ez.my_op","My Operator",lambda world: print("Hello world"))

=========================
Creating a triangle mesh
=========================

Registers an operator that creates a triangle mesh and UV-maps it

.. code-block:: python

    def create_triangle(world):
        mesh = world.create_mesh("triangle")
        
        # Creates vertices forming a triangle
        mesh.add_vertex((0,0,0))
        mesh.add_vertex((10,0,0))
        mesh.add_vertex((0,10,0))

        # Adds a face between the first 3 vertices
        mesh.add_face([0,1,2])
       
        # Adds uv coordinates to all three vertices on the face
        layer = mesh.add_uv_layer() 
        g.set_uv_coordinate(layer,0,0,(0,0))
        g.set_uv_coordinate(layer,0,1,(1,0))
        g.set_uv_coordinate(layer,0,2,(0,1))

    def init(registry):
        registry.register_operator("ez.create_triangle","Create Triangle",create_triangle)


===============================
Creating an animated armature
===============================

Registers an operator that creates an armature with a single bone that rotates 90 degrees on the x-axis

.. code-block:: python

    def create_armature(world):
        armature = world.create_armature("armature")

        # Creates a bone from (0,0,0) to (1,0,0) 
        bone = armature.create_bone("bone",(0,0,0),(1,0,0))

        # Poses the bone to "not rotate" at frame 0
        bone.insert_rotation_frame("action",0,(0,0,0))

        # Poses the bone to rotate 90 degrees by frame 10
        bone.insert_rotation_frame("action",10,(1.57,0,0))

    def init(registry):
        registry.register_operator("ez.create_armature","Create Armature",create_armature)