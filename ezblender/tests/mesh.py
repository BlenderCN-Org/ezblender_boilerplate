def test_add_vertex(world,tester):
    TEST_X_VALUE = 10

    m0 = world.create_mesh("mesh")
    tester.does_not_throw(lambda: m0.add_vertex((TEST_X_VALUE,0,0)),"Can start adding vertices after world#create_mesh")
    tester.equal(m0.get_vertex(0).co.x,TEST_X_VALUE,"Has valid vertex data after #add_vertex")

    m1 = world.create_mesh("mesh1")
    tester.does_not_throw(lambda: m1.add_vertex((TEST_X_VALUE,0,0)),"Can start adding vertices on multiple meshes")
    tester.equal(m1.get_vertex(0).co.x,TEST_X_VALUE,"Has valid vertex data after #add_vertex")

def test_add_edge(world,tester):
    m0 = world.create_mesh("mesh")

    m0.add_vertex((0,0,0))
    m0.add_vertex((10,0,0))
    m0.add_vertex((20,0,0))

    tester.throws(lambda: m0.add_edges([0,4]),"Throws on invalid indices")
    tester.does_not_throw(lambda: m0.add_edges([0,1,2]),"Does not throw on valid indices")

def test_add_face(world,tester):
    m0 = world.create_mesh("mesh")
    m0.add_vertex((0,0,0))
    m0.add_vertex((10,0,0))
    m0.add_vertex((20,0,0))
    tester.throws(lambda: m0.add_face([0,1,3]),"Throws on invalid indices")
    tester.does_not_throw(lambda: m0.add_face([0,1,2,]),"Does not throw on valid indices")

def test_add_vertex_groups(world,tester):
    m0 = world.create_mesh("mesh")
    m0.add_vertex((0,0,0))
    m0.set_vertex_groups(0,[("group1",0.5),("group2",0.25)])
    groups = m0.get_groups_for_vertex(0)
    tester.equal(groups,[(0,0.5),(1,0.25)],"Groups can be found per vertex")

def test_add_uv_layers(world,tester):
    m0 = world.create_mesh("mesh")
    m0.add_vertex((0,0,0))
    m0.add_vertex((10,0,0))
    m0.add_vertex((0,10,0))
    m0.add_face([0,1,2])
    layer = m0.add_uv_layer()
    m0.set_uv_coordinate(layer,0,0,(10,20))
    tester.equal(m0.get_uv_coordinate(layer,0,0),(10,20))