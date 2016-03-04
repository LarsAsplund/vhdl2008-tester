from vunit import VUnit

vu = VUnit.from_argv()
lib = vu.add_library("lib")
lib.add_source_files("tb_fixed_generic_pkg.vhd")
vu.main()
