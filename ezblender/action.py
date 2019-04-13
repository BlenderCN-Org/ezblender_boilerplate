import importlib

from . import vector
try: importlib.reload(vector)
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

Vector = vector.Vector

class Action:
    def __init__(self,world,blender_action):
        self.world = world
        self.blender_action = blender_action

    def get_name(self):
        return self.blender_action.name

    def set_curve_value(self,group,name,frame,value,interpolation='LINEAR'):
        if type(value) is float or type(value) is int:
            value = Vector([value]).values
        else:
            value = Vector(value).values
        for (i,value) in enumerate(value):
            curve = self.blender_action.fcurves.find(name,i)
            if curve is None:
                curve = self.blender_action.fcurves.new(name,i,group)
            kf = curve.keyframe_points.insert(frame,value)
            kf.interpolation = interpolation

    def get_curve_value(self,name,frame):
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