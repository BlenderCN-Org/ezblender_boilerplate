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
        self.name = self.blender_bone.name

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

    def set_parent(self,parent,attach_head=False):
        """Sets the parent of this bone
            Args:
                parent (Bone) : The new parent for this bone
                attach_head (boolean) : Whether to attach the head of this bone to the new parent
        """
        self.blender_bone.parent = parent.blender_bone
        if(attach_head):
            self.set_head(parent.get_tail())

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

    def insert_location_frame(self,action,time,value,interpolation='LINEAR'):
        """Inserts a new location pose frame for this bone

        Args:
            action (string): Name of the 'action' (as seen in the 'Action editor') to assign to
            time (float): Time value for the inserted frame
            value (Vector): Vector of 3 or 4 values, depending on the rotation type
            mode (string): Rotation mode to use ('XYZ','QUATERNION','AXIS_ANGLE')
            interpolation (string): Interpolation to use for this rotation TODO add examples
        """
        action = self.armature.world.get_action(action)
        action.set_curve_value(self.name,"pose.bones[\""+self.name+"\"].location",time,value)

    def insert_scale_frame(self,action,time,value,interpolation='LINEAR'):
        """Inserts a new scale pose frame for this bone

        Args:
            action (string): Name of the 'action' (as seen in the 'Action editor') to assign to
            time (float): Time value for the inserted frame
            value (Vector): Vector of 3 or 4 values, depending on the rotation type
            mode (string): Rotation mode to use ('XYZ','QUATERNION','AXIS_ANGLE')
            interpolation (string): Interpolation to use for this rotation TODO add examples
        """
        action = self.armature.world.get_action(action)
        action.set_curve_value(self.name,"pose.bones[\""+self.name+"\"].scale",time,value)

    def insert_rotation_frame(self,action,time,value,mode='XYZ',interpolation='LINEAR'):
        """Inserts a new rotation pose frame for this bone

        Args:
            action (string): Name of the 'action' (as seen in the 'Action editor') to assign to
            time (float): Time value for the inserted frame
            value (Vector): Vector of 3 or 4 values, depending on the rotation type
            mode (string): Rotation mode to use ('XYZ','QUATERNION','AXIS_ANGLE')
            interpolation (string): Interpolation to use for this rotation TODO add examples
        """
        self.armature.__begin_pose_mode__()
        pbone = self.armature.blender_object.pose.bones[self.name]
        pbone.rotation_mode = mode
        action = self.armature.world.get_action(action)

        rotation_name = None
        if mode== 'XYZ':
            rotation_name = 'euler'
        elif mode == 'QUATERNION':
            rotation_name = 'quaternion'
        else:
            raise Exception('Unknown rotation mode: '+mode)

        action.set_curve_value(self.name,"pose.bones[\""+self.name+"\"].rotation_"+rotation_name,time,value)