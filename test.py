import os
import imp
import inspect

obj_list = []


def main():

	dir_path = os.path.dirname(os.path.realpath(__file__))
	pattern = "*.py"

	for path, subdirs, files in os.walk(dir_path):
		for name in files:
			if fnmatch(name):
				found_module = imp.find_module(name[:-3], [path])
				module = imp.load_module(name, found_module[0], found_module[1], found_module[2])
				for mem_name, obj in inspect.getmembers(module):
					if inspect.isclass(obj) and inspect.getmodule(obj) is module:
						obj_list.append(obj())

def fnmatch(file):
	if ".py" in file:
		file = file[:-3]
		print(file)

main()