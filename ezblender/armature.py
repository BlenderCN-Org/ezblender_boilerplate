import bpy

class Armature:
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
        bone = self.blender_object.data.edit_bones.new(name)
        bone.head = head
        bone.tail = tail