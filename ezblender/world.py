import bpy
import time
import importlib
from . import mesh

try: importlib.reload(mesh) 
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

class World:
	"""
	Represents global access to the EZBlender system
	"""
	def __init__(self):
		# TODO: Better checking for object/edit mode
		try:
			bpy.ops.object.mode_set(mode='OBJECT')
		except:
			pass

		self.current_edit_object = None
		self.kept_objects = {}

	def __set_edit_object__(self,obj):
		self.current_edit_object = obj

	def __set_object_mode__(self):
		if self.current_edit_object!=None:
			self.current_edit_object.__finish_edit_mode__()
			self.current_edit_object = None

	def __createobject__(self,name,objtype):
		# TODO: Does not remove mesh/armature children properly
		self.remove(name)
		obj = bpy.data.objects.new(name,objtype)
		scene = bpy.context.scene
		scene.objects.link(obj)
		obj.name = name
		return obj

	def remove(self,name):
		self.__set_object_mode__()
		"""Removes a single object from the Blender scene.

		Args:
			name (string): Name of the object to be removed
		"""
		if not name in bpy.data.objects:
			return
		if name in self.kept_objects:
			del self.kept_objects[name]
		bpy.ops.object.select_all(action='DESELECT')
		bpy.data.objects[name].select = True
		bpy.ops.object.delete()

	def remove_everything(self):
		self.__set_object_mode__()
		"""Removes all objects from the Blender scene.
		"""
		self.kept_objects = {}

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
		if name in self.kept_objects:
			return self.kept_objects[name]

		obj = bpy.data.objects[name]
		if obj.type=='MESH':
			return mesh.Mesh(self,obj)
		else:
			return obj

	def has_object(self,name):
		"""Check if an object exists in the Blender scene.

		Args:
			name (string): Name of the object
		
		Returns:
			boolean: True when object with name exists
		"""
		return name in bpy.data.objects

	def create_armature(self,name):
		self.__set_object_mode__()
		"""Creates a new Armature in the Blender scene.

		Warning:
			Removes any previous object of this name

		Args:
			name (string): Name of the new object	
		"""
		obj = self.__createobject__(name,bpy.data.armatures.new('Armature'))
		self.kept_objects[name] = obj
		return obj

	def create_mesh(self,name):
		self.__set_object_mode__()
		"""Creates a new mesh in the Blender scene.

		Warning: 
			Removes any previous object of this name	

		Args:
			name (string): Name of the new object
		"""
		obj = mesh.Mesh(self,self.__createobject__(name,bpy.data.meshes.new('mesh')))
		self.kept_objects[name] = obj
		return obj 