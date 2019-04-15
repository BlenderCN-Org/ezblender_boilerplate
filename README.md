# ezblender-boilerplate

**ezblender is still under heavy development, breaking changes are common**

ezblender is a simple wrapper module to make developing Blender addons simpler. It provides a separate and greatly simplified interface to some of the most common Blender operations, such as creating objects, modifying meshes, and inserting animation keyframes.

## Prerequisites
* Blender version 2.79
* Basic knowledge of the Python programming language
* Basic knowledge of Blender

## Installation/Setup

1. Navigate to your blender addons folder: `Blender/2.79/scripts/addons`<br/><br/>
2. Clone/extract this repository into the `Blender/2.79/scripts/addons` folder (so that it now contains the folder `ezblender_boilerplate`)<br/><br/>
2.1. **Optional:** rename the `ezblender_boilerplate` folder to the name of your own addon<br/><br/>
2.2. **Optional:** Navigate into `ezblender_boilerplate` and open the file `__init__.py`, here you can change some basic addon fields: addon name, author and category right at the top.<br/><br/>
3. Start Blender and open the addons settings window, search for `EZBlender` (or your new name) and enable the addon

## Writing your addon

**Under construction**

Navigate to your `ezblender_boilerplate` folder and open the file `addon.py`, this is the entry point for your addon. 

It should currently look like this: 

```
def init(registry):
  pass
```

To make the addon *do* something, we can use this function to registers some operators

```
def init(registry):
  registry.register_operator("ezblender.my_operator","My Operator",lambda world: print("Hello world"))
```

If we reload the addon in blender (Bound to the F8 key by default), we can open the operator menu (Space) and search for "My Operator". Running it should print "Hello World" to the System Console (Window->Toggle System Console)
