import bpy

class World:
	"""
	Represents global access to the EZBlender system
	"""
	def remove(self,name):
		"""Removes a single object from the Blender scene.
		
		Args:
			name (string): Name of the object to be removed
		"""
		if not name in bpy.data.objects:
			return
		bpy.ops.object.select_all(action='DESELECT')
		bpy.data.objects[name].select = True
		bpy.ops.object.delete()

	def remove_everything(self):
		"""Removes all objects from the Blender scene.
		"""
		bpy.ops.object.select_all(action='SELECT')
		bpy.ops.object.delete()

	def create_mesh(self,name):
		"""Creates a new mesh in the Blender scene.

		Warning: 
			Removes any oprevious object of this name	

		Args:
			name (string): Name of the new object
		"""
		self.remove(name)
		bpy.data.meshes.new("mesh")