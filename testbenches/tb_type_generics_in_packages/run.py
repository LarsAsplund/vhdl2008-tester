from vunit import VUnit
from os.path import join, dirname

vu = VUnit.from_argv()
lib = vu.add_library('lib')
lib.add_source_files(join(dirname(__file__), '*.vhd'))
vu.main()
