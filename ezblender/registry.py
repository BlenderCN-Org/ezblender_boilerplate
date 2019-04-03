import bpy
import importlib
from . import world
try: importlib.reload(world) 
except: pass # Try/catch to work with Sphinx documentation

class Registry:
	"""
	Object used to register operators to the Blender addon
	"""
	registered_operators = []
	reg_world = world.World()

	def register_operator(self,id,label,operator):
		"""Registers a new operator to blender

		Args:
			id (int): 
			label: 
			operator: 
		"""
		rworld = self.reg_world
		class OperatorClass(bpy.types.Operator):
			bl_idname = id
			bl_label = label
			bl_options = {'REGISTER','UNDO'}
			def execute(self,context):
				operator(rworld)
				return {'FINISHED'}

		self.registered_operators.append(OperatorClass)