def test_create_action(world,tester):
    tester.does_not_throw(lambda:world.create_action("action"),"Does not throw when creating new action")
    tester.does_not_throw(lambda:world.create_action("action"),"Does not throw when recreating old action")
    tester.not_none(world.get_action("action"),"Updates after action creation")

def test_set_curve_value(world,tester):
    action = world.create_action("action")
    action.set_curve_value("group","curve",25,100)
    tester.equal(action.get_curve_value("curve",25),100)

def test_set_curve_value_multi(world,tester):
    action = world.create_action("action")
    action.set_curve_value("group","curve",25,(100,150,200))
    tester.equal(action.get_curve_value("curve",25),(100,150,200))