import os

def test_write_integers(world,tester):
    testpath = os.path.join(os.path.dirname(__file__),'test.testfile')
    file = world.write_binary_file(testpath)
    file.write_int8(25)
    file.write_int16(50)
    file.write_int32(75)
    file.write_int64(100)
    file.write_string('abcdefg')
    file.write_int8(0)
    file.write_string('lol')
    file.write_int8(0)
    file.close()

    file = world.read_binary_file(testpath)

    tester.equal(file.read_int8(),25)
    tester.equal(file.read_int16(),50)
    tester.equal(file.read_int32(),75)
    tester.equal(file.read_int64(),100)
    tester.equal(file.read_string(7),'abcdefg')
    tester.equal(file.read_int8(),0)
    tester.equal(file.read_terminated_string(),'lol')
    file.close()