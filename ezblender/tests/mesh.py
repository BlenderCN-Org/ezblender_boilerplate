def test_add_vertex(world,tester):
    TEST_X_VALUE = 10

    m0 = world.create_mesh("mesh")
    tester.does_not_throw(lambda: m0.add_vertex((TEST_X_VALUE,0,0)),"Can start adding vertices after world#create_mesh")
    tester.equal(m0.get_vertex(0).co.x,TEST_X_VALUE,"Has valid vertex data after #add_vertex")

    m1 = world.create_mesh("mesh1")
    tester.does_not_throw(lambda: m1.add_vertex((TEST_X_VALUE,0,0)),"Can start adding vertices on multiple meshes")
    tester.equal(m1.get_vertex(0).co.x,TEST_X_VALUE,"Has valid vertex data after #add_vertex")