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
                getattr(thismod,fun)(generator(),tester)

def transtest_set_local_location(obj,tester):
    tester.equal(obj.get_local_location(),(0,0,0),"Initializes to 0,0,0")

    obj.set_local_location((5,5,5))
    tester.equal(obj.get_local_location(),(5,5,5),"Updates local after single call")
    tester.equal(obj.get_global_location(),(5,5,5),"Updates global after single call")

    obj.set_local_location((10,10,5))
    tester.equal(obj.get_local_location(),(10,10,5),"Updates local after multiple calls")
    tester.equal(obj.get_global_location(),(10,10,5),"Updates local after multiple calls")

def transtest_set_global_location(obj,tester):
    tester.equal(obj.get_global_location(),(0,0,0),"Initializes to 0,0,0")

    obj.set_global_location((3,3,3))
    tester.equal(obj.get_local_location(),(3,3,3),"Updates local after single call")
    tester.equal(obj.get_global_location(),(3,3,3),"Updates global after single call")

def transtest_set_local_rotation(obj,tester):
    tester.equal(obj.get_local_rotation("XYZ"),(0,0,0),"Initializes to 0,0,0 euler")