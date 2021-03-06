import sys
thismod = sys.modules[__name__]

def test_run(world_in,tester):
    objs = [
        ("mesh",lambda:world_in.create_mesh("mesh")),
        ("armature",lambda:world_in.create_armature("armature"))
    ]

    for (name,generator) in objs:
        for fun in dir(thismod):
            if fun.startswith('transtest_'):
                tester.set_test(name,fun)
                world_in.remove_everything()                
                getattr(thismod,fun)(generator(),world_in,tester)

def transtest_set_local_location(obj,world,tester):
    tester.equal(obj.get_local_location(),(0,0,0),"Initializes to 0,0,0")

    obj.set_local_location((5,5,5))
    tester.equal(obj.get_local_location(),(5,5,5),"Updates local after single call")
    tester.equal(obj.get_global_location(),(5,5,5),"Updates global after single call")

    obj.set_local_location((10,10,5))
    tester.equal(obj.get_local_location(),(10,10,5),"Updates local after multiple calls")
    tester.equal(obj.get_global_location(),(10,10,5),"Updates local after multiple calls")

def transtest_set_global_location(obj,world,tester):
    tester.equal(obj.get_global_location(),(0,0,0),"Initializes to 0,0,0")

    obj.set_global_location((3,3,3))
    tester.equal(obj.get_local_location(),(3,3,3),"Updates local after single call")
    tester.equal(obj.get_global_location(),(3,3,3),"Updates global after single call")

def transtest_set_local_rotation(obj,world,tester):
    EULER = (10,3,4)
    QUAT = (-0.878113329410553, -0.22905924916267395, -0.17942853271961212, -0.3798081874847412)
    AXIS = (1,2,3,4)

    tester.equal(obj.get_local_rotation("XYZ"),(0,0,0),"Initializes to 0,0,0 euler")
    obj.set_local_rotation(EULER)
    tester.equal(obj.get_local_rotation("XYZ"),EULER,'Updates xyz after single xyz rotation')
    tester.equal(obj.get_local_rotation("QUATERNION"),QUAT,'Updates quaternion after single xyz rotation')

    obj.set_local_rotation((0,0,0),'XYZ')
    tester.equal(obj.get_local_rotation("XYZ"),(0,0,0),"Reinitializes to 0,0,0 euler")
    obj.set_local_rotation(QUAT,'QUATERNION')

    tester.equal(obj.get_local_rotation("QUATERNION"),QUAT,'Updates quaternion after single quaternion rotation')

    obj.set_local_rotation(AXIS,'AXIS_ANGLE')
    tester.equal(obj.get_local_rotation("AXIS_ANGLE"),AXIS)

def transtest_set_parent(obj,world,tester):
    cube = world.create_mesh("cube")
    obj.set_parent(cube)
    tester.equal(cube,obj.get_parent(),"Updates parent after single call")

    cube1 = world.create_mesh("cube1")
    obj.set_parent(cube1)
    tester.not_equal(cube,obj.get_parent(),"Does not keep old parent after another call")
    tester.equal(cube1,obj.get_parent(),"Updates parent after multiple calls")

def transtest_set_scale(obj,world,tester):
    obj.set_local_scale((1,5,1))
    tester.equal(obj.get_local_scale(),(1,5,1))