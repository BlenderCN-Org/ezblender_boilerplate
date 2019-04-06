def test_create_mesh(world,tester):
	MESHNAME = "mesh"

	mesh0 = world.create_mesh(MESHNAME)
	mesh1 = world.get_object(MESHNAME)
	tester.equal(mesh0,mesh1,"Created mesh can be accessed by #get_object")

	mesh2 = world.create_mesh(MESHNAME)
	mesh3 = world.get_object(MESHNAME)
	tester.equal(mesh2,mesh3,"Overwriting mesh is retrieved by #get_object")

def test_create_armature(world,tester):
	ARMATURE_NAME = "armature"

	arma0 = world.create_armature(ARMATURE_NAME)
	arma1 = world.get_object(ARMATURE_NAME)
	tester.equal(arma0,arma1,"Created armature can be accessed by #get_object")
	
	arma2 = world.create_armature(ARMATURE_NAME)
	arma3 = world.get_object(ARMATURE_NAME)
	tester.equal(arma2,arma3,"Overwriting armature is retrieved by #get_object")