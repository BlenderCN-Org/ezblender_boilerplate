import importlib

from . import vector
importlib.reload(vector)
Vector = vector.Vector

class Bone:
    def __init__(self,armature,blender_bone):
        self.armature = armature
        self.blender_bone = blender_bone

    def set_head(self,head):
        self.armature.__begin_edit_mode__()
        self.blender_bone.head = Vector(head).values
    
    def set_tail(self,tail):
        self.armature.__begin_edit_mode__()
        self.blender_bone.tail = Vector(tail).values

    def get_head(self):
        self.armature.__begin_edit_mode__()
        return Vector(self.blender_bone.head)
    
    def get_tail(self):
        self.armature.__begin_edit_mode__()
        return Vector(self.blender_bone.tail)