import importlib
import mathutils
from inspect import getframeinfo, stack
import sys

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
	
	def equal_vec(self,a,b,message=""):
		if(type(a)==tuple):
			a = mathutils.Vector(a)
		if(type(b)==tuple):
			b = mathutils.Vector(b)
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

def _get_test_module():
	return __name__.replace('tester','')+'tests.'

def _single_test(world_in,tester,testname):
	mod = importlib.import_module(_get_test_module()+testname)
	importlib.reload(mod)
	for fun in dir(mod):
		if fun.startswith('test_'):
			tester.set_test(testname,fun)
			world_in.remove_everything()
			getattr(mod,fun)(world_in,tester)

def runtests(world_in):
	tester = Tester()

	# TODO Removed test functions aren't unloaded by importlib.reload
	_single_test(world_in,tester,'world')
	_single_test(world_in,tester,'mesh')
	_single_test(world_in,tester,'armature')
	_single_test(world_in,tester,'transformable')

	# Clean up
	world_in.remove_everything()
	tester.print_results()