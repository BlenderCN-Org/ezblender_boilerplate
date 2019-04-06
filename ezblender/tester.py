import importlib
from inspect import getframeinfo, stack

class Tester:
	def __init__(self):
		self.modules = {}

	def __add_result(self,success,message):
		# Caller is two function calls above
		lineno = str(getframeinfo(stack()[2][0]).lineno)
		self.cur_test.append((success,message,lineno))

	def true(self,val,message=""):
		self.__add_result(val==True,message)

	def false(self,val,message=""):
		self.__add_result(val==False,message)

	def equal(self,a,b,message=""):
		self.__add_result(a==b,message)

	def not_equal(self,a,b,message=""):
		self.__add_result(a!=b,message)

	def throws(self,fun,message=""):
		try:
			fun()
			self.__add_result(False,message)
		except:
			self.__add_result(True,message)

	def does_not_throw(self,fun,message=""):
		try:
			fun()
			self.__add_result(True,message)
		except:
			self.__add_result(False,message)

	def set_test(self,module,test):
		cur_module = None
		if not module in self.modules:
			cur_module = {}
			self.modules[module] = cur_module
		else:
			cur_module = self.modules[module]

		if not test in cur_module:
			self.cur_test = []
			cur_module[test] = self.cur_test
		else:
			self.cur_test = cur_module[test]	

	def print_results(self):
		print("Test report:")
		for (modulename,module) in self.modules.items():
			print('  '+modulename)
			for (testname,test) in module.items():
				print('    '+testname)
				for (success,message,lineno) in test:
					if not success:
						print('      ERROR: '+message+' (line '+lineno+')')

def runtests(world_in):
	tester = Tester()

	# TODO: Removed test functions aren't unloaded by importlib.reload

	from .tests import world
	importlib.reload(world)

	for fun in dir(world):
		if fun.startswith('test_'):
			tester.set_test('world',fun)
			world_in.remove_everything()
			getattr(world,fun)(world_in,tester)

	from .tests import mesh
	importlib.reload(mesh)

	for fun in dir(mesh):
		if fun.startswith('test_'):
			tester.set_test('mesh',fun)
			world_in.remove_everything()
			getattr(mesh,fun)(world_in,tester)

	world_in.remove_everything()
	tester.print_results()