import bpy

class Registry:
	registered_operators = []

	def register_operator(self,id,label,operator):
		class OperatorClass(bpy.types.Operator):
			bl_idname = id
			bl_label = label
			bl_options = {'REGISTER','UNDO'}
			def execute(self,context):
				operator()
				return {'FINISHED'}

		self.registered_operators.append(OperatorClass)