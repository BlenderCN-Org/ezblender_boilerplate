import bpy
import importlib

from . import scene_object
importlib.reload(scene_object)

from . import vector
importlib.reload(vector)
Vector = vector.Vector

from . import bone
importlib.reload(bone)

class Armature(scene_object.SceneObject):
    """
    Represents a single armature object in the Blender Scene
    """
    def __init__(self,world,blender_object):
        self.world = world
        self.blender_object = blender_object

    def __begin_edit_mode__(self):
        if(self.world.current_edit_object==self):
            return
        self.world.current_edit_object = self
        bpy.context.scene.objects.active = self.blender_object
        bpy.ops.object.mode_set(mode='EDIT')

    def __finish_edit_mode__(self):
        bpy.ops.object.mode_set(mode='OBJECT')

    def create_bone(self,name,head,tail):
        """Adds a new bone to this armature

        Args:
            name (string) : Name of the new bone
            head ((float,float,float)) : Location of the "head" of the bone
            tail ((float,float,float)) : Location of the "tail" of the bone
        """
        self.__begin_edit_mode__()
        a_bone = self.blender_object.data.edit_bones.new(name)
        a_bone.head = Vector(head).values
        a_bone.tail = Vector(tail).values
        return bone.Bone(self,a_bone)