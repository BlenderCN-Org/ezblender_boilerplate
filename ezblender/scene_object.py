import bpy
import importlib

from . import transformable
try: importlib.reload(transformable)
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

from . import vector
try: importlib.reload(vector)
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

Vector = vector.Vector

class SceneObject(transformable.Transformable):
    """
    Represents a single mesh or armature in the Blender Scene
    """
    def __get_global_location__(self):
        bpy.context.scene.update()
        return Vector(self.blender_object.matrix_world.translation)

    def __get_local_location__(self):
        return Vector(self.blender_object.location)

    def __set_local_location__(self,location):
        self.blender_object.location = Vector(location).values

    def __set_global_location__(self,location):
        location = Vector(location)
        prev = self.__get_local_location__()
        diff = location-self.__get_global_location__()
        self.__set_local_location__(prev+diff)

    def __set_rotation_mode__(self,mode):
        self.blender_object.rotation_mode = mode

    def __get_local_rotation__(self,mode="XYZ"):
        self.__set_rotation_mode__(mode)
        # TODO add other xyz permutations
        if mode == "XYZ":
            return Vector(self.blender_object.rotation_euler)
        elif mode == "QUATERNION":
            return Vector(self.blender_object.rotation_quaternion)
        elif mode == "AXIS_ANGLE":
            return Vector(tuple(self.blender_object.rotation_axis_angle))

    def __set_local_rotation__(self,rotation,mode="XYZ"):
        self.__set_rotation_mode__(mode)
        if mode == "XYZ":
            self.blender_object.rotation_euler = Vector(rotation).values
        elif mode == "QUATERNION":
            self.blender_object.rotation_quaternion = Vector(rotation).values
        elif mode == "AXIS_ANGLE":
            self.blender_object.rotation_axis_angle = Vector(rotation).values