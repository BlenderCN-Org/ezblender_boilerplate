import importlib

from . import vector
try: importlib.reload(vector)
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

Vector = vector.Vector

class Action:
    """
    Represents a single 'Action', as can be found in the Blender Dope Sheet/Action Editor view
    """
    def __init__(self,world,blender_action):
        self.world = world
        self.blender_action = blender_action

    def get_name(self):
        """Returns the name of this action

            Returns:
                (string) : Action name
        """
        return self.blender_action.name

    def set_curve_value(self,group,name,frame,value,interpolation='LINEAR'):
        """Sets a curve value in this action

            Args:
                group (string): Group name of the curve, if created
                name (string): Name of the curve to insert the values to
                frame (float): Time value to insert to
                value (Vector): Value or values to insert to this curve
        """
        value = Vector(value).values
        for (i,value) in enumerate(value):
            curve = self.blender_action.fcurves.find(name,i)
            if curve is None:
                curve = self.blender_action.fcurves.new(name,i,group)
            kf = curve.keyframe_points.insert(frame,value)
            kf.interpolation = interpolation

    def get_curve_value(self,name,frame):
        """Returns the curve values at some frame in a curve

            Args:
                name (string): Name of the curve to search
                frame (float): Time value to search at

            Returns:
                (Vector): Vector containing all values found at this timeframe in this curve.
        """
        curves = []
        i = 0
        while True:
            curve = self.blender_action.fcurves.find(name,i)
            if curve is None:
                break
            else:
                curves.append(curve) 
                i = i + 1

        values = []
        for curve in curves:
            for kf in curve.keyframe_points:
                if(kf.co.x==frame):
                    values.append(kf.co.y)
                    break 
        return Vector(values)