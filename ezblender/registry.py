import bpy
import importlib
from . import world
importlib.reload(world)


class Registry:
	registered_operators = []
	reg_world = world.World()

	def register_operator(self,id,label,operator):
		rworld = self.reg_world
		class OperatorClass(bpy.types.Operator):
			bl_idname = id
			bl_label = label
			bl_options = {'REGISTER','UNDO'}
			def execute(self,context):
				operator(rworld)
				return {'FINISHED'}

		self.registered_operators.append(OperatorClass)