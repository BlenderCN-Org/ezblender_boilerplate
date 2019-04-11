import bpy
import importlib

from . import transformable
importlib.reload(transformable)

class SceneObject(transformable.Transformable):
    """
    Represents a single mesh or armature in the Blender Scene
    """
    def __get_global_location__(self):
        bpy.context.scene.update()
        return self.blender_object.matrix_world.translation

    def __get_local_location__(self):
        return self.blender_object.location

    def __set_local_location__(self,location):
        self.blender_object.location = self.__make_vector__(location) 

    def __set_global_location__(self,location):
        location = self.__make_vector__(location)
        prev = self.__get_local_location__()
        diff = location-self.__get_global_location__()
        self.__set_local_location__(prev+diff)