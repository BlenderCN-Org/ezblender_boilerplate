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