import importlib

from . import transformable
try: importlib.reload(transformable)
except Exception as e: print("Exception Reloading",e) # Try/catch to work with Sphinx documentation

from . import vector
try: importlib.reload(vector)
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

Vector = vector.Vector

class Bone:
    """
    Represents a single bone in an Armature
    """
    def __init__(self,armature,blender_bone):
        self.armature = armature
        self.blender_bone = blender_bone

    def set_head(self,head):
        """Sets the Head location of this bone

        Args:
            head (Vector|(float,float,float)): Head location
        """
        self.armature.__begin_edit_mode__()
        self.blender_bone.head = Vector(head).values
    
    def set_tail(self,tail):
        """Sets the Tail location of this bone

        Args:
            head (Vector|(float,float,float)): Tail location
        """
        self.armature.__begin_edit_mode__()
        self.blender_bone.tail = Vector(tail).values

    def get_head(self):
        """Returns the head location of this bone

        Returns:
            Vector: head location
        """
        self.armature.__begin_edit_mode__()
        return Vector(self.blender_bone.head)
    
    def get_tail(self):
        """Returns the tail location of this bone

        Returns:
            Vector: tail location
        """
        self.armature.__begin_edit_mode__()
        return Vector(self.blender_bone.tail)

    def insert_rotation_frame(self,action,time,value,mode='XYZ',interpolation='LINEAR'):
        """Inserts a new "pose" frame for this bone
        """
        self.armature.__begin_edit_mode__()
        bonename = self.blender_bone.name
        self.armature.__begin_pose_mode__()
        pbone = self.armature.blender_object.pose.bones[bonename]
        pbone.rotation_mode = mode
        action = self.armature.world.get_action(action)
        name = self.blender_bone.name

        rotation_name = None
        if mode== 'XYZ':
            rotation_name = 'euler'
        elif mode == 'QUATERNION':
            rotation_name = 'quaternion'
        else:
            raise Exception('Unknown rotation mode: '+mode)

        action.set_curve_value(name,"pose.bones[\""+name+"\"].rotation_"+rotation_name,time,value)