import bpy
import importlib

from bpy_extras.io_utils import (
	ImportHelper,
	ExportHelper
)

from . import world
try: importlib.reload(world) 
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

from bpy.props import (
	BoolProperty
)

class Registry:
	"""
	Object used to register operators to the Blender addon
	"""
	registered_operators = []
	registered_export_windows = []
	registered_import_windows = []
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
				rworld.__set_object_mode__()
				return {'FINISHED'}

		self.registered_operators.append(OperatorClass)

	def register_export_window(self,id,label,extension,operator):
		"""Registers a new 'export' window to blender

		Args:
			id (int):
			label:
			operator:
		"""
		rworld = self.reg_world
		class ExportWindowClass(bpy.types.Operator,ExportHelper):
			bl_idname = id
			bl_label = label
			bl_options = {'PRESET'}

			filename_ext = extension

			def execute(self,context):
				keywords = self.as_keywords()
				operator(rworld,keywords)
				rworld.__set_object_mode__()
				return {'FINISHED'}

		def export_fun(self,context):
			self.layout.operator(id,text=label)

		self.registered_operators.append(ExportWindowClass)
		self.registered_export_windows.append(export_fun)

	def register_import_window(self,id,label,extension,operator):
		"""Registers a new 'import' window to blender

		Args:
			id (int):
			label:
			operator:
		"""
		rworld = self.reg_world
		class ImportWindowClass(bpy.types.Operator,ImportHelper):
			bl_idname = id
			bl_label = label
			bl_options = {'PRESET'}

			filename_ext = extension

			def execute(self,context):
				keywords = self.as_keywords()
				operator(rworld,keywords)
				rworld.__set_object_mode__()
				return {'FINISHED'}
		def import_fun(self,context):
			self.layout.operator(id,text=label)

		self.registered_operators.append(ImportWindowClass)
		self.registered_import_windows.append(import_fun)