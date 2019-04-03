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

def register():
	addon.init()
	pass

def unregister():
	pass