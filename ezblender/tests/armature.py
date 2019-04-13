def test_create_bone(world,tester):
    arma = world.create_armature("armature")

    tester.does_not_throw(
        lambda:arma.create_bone("bone",(0,0,0),(10,0,0)),
        "Can create bone immediately after creation"
    )

    tester.does_not_throw(
        lambda:arma.create_bone("bone",(10,0,0),(20,0,0)),
        "Can create multiple bones of the same name"
    )

def test_bone_set_head_tail(world,tester):
    arma = world.create_armature("armature")
    bone = arma.create_bone("bone",(0,0,0),(0,0,0))

    tester.equal(bone.get_head(),(0,0,0),"Head is initialized correctly")
    tester.equal(bone.get_tail(),(0,0,0),"Tail is initialized correctly")

def test_bone_set_parent(world,tester):
    arma = world.create_armature("armature")
    bone = arma.create_bone("bone",(0,0,0),(10,0,0))
    bone1 = arma.create_bone("bone1",(0,0,0),(5,0,0))
    bone.set_parent(bone1)
    tester.equal(bone.get_head(),(0,0,0),"Head is not moved without specifying it to")
    bone.set_parent(bone1,True)
    tester.equal(bone.get_head(),(5,0,0),"Head is moved if specified to")
    tester.equal(bone.get_tail(),(10,0,0),"Tail is not moved at all")