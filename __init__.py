""" Change these fields to fit your addon"""
bl_info = {
	"name" : "EZBlender Boilerplate",
	"author" : "Anton Ohlsson",
	"category" : "Addon"
}

""" OPEN 'addon.py', DO NOT CHANGE ANYTHING BELOW THIS LINE """

import bpy
import importlib

from . import addon
importlib.reload(addon)

from .ezblender import registry
importlib.reload(registry)

cur_registry = registry.Registry()

def register():
	addon.init(cur_registry)
	for operator in cur_registry.registered_operators:
		bpy.utils.register_class(operator)

def unregister():
	for operator in cur_registry.registered_operators:
		bpy.utils.unregister_class(cls)
	cur_registry.registered_classes.clear()