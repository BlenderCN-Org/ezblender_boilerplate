import bpy
import time

class World:
	"""
	Represents global access to the EZBlender system
	"""

	def __createobject__(self,name,objtype):
		# TODO: Does not remove mesh/armature children properly
		self.remove(name)
		obj = bpy.data.objects.new(name,objtype)
		scene = bpy.context.scene
		scene.objects.link(obj)
		obj.name = name
		return obj

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
		# TODO: Does not remove animation data
		for scene in bpy.data.scenes:
			for obj in scene.objects:
				scene.objects.unlink(obj)

		# only worry about data in the startup scene
		for bpy_data_iter in (
			bpy.data.objects,
			bpy.data.meshes,
			bpy.data.lamps,
			bpy.data.cameras,
			):
			for id_data in bpy_data_iter:
				bpy_data_iter.remove(id_data)

	def get_object(self,name):
		"""Returns an existing Object in the Blender scene.

		Args:
			name (string): Name of the existing object

		Returns:
			TODO: Blender object(?)
		
		"""
		return bpy.data.objects[name]

	def create_armature(self,name):
		"""Creates a new Armature in the Blender scene.

		Warning:
			Removes any previous object of this name

		Args:
			name (string): Name of the new object	
		"""
		return self.__createobject__(name,bpy.data.armatures.new('Armature'))

	def create_mesh(self,name):
		"""Creates a new mesh in the Blender scene.

		Warning: 
			Removes any previous object of this name	

		Args:
			name (string): Name of the new object
		"""
		return self.__createobject__(name,bpy.data.meshes.new('mesh'))
