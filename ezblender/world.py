import bpy

class World:
	def remove(self,name):
		if not name in bpy.data.objects:
			return
		bpy.ops.object.select_all(action='DESELECT')
		bpy.data.objects[name].select = True
		bpy.ops.object.delete()

	def remove_everything(self):
		bpy.ops.object.select_all(action='SELECT')
		bpy.ops.object.delete()

	def create_mesh(self,name):
		self.remove(name)
		bpy.data.meshes.new("mesh")