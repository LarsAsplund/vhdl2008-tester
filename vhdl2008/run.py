import unittest
from vunit import VUnit
from os.path import join, dirname

class TestVHDL2008Support(unittest.TestCase):
    def test_matching_operator(self):
        self.check('tb_matching_operator.vhd')

    def test_condition_operator(self):
        self.check('tb_condition_operator.vhd')

    def test_fixed_generic_pkg(self):
        self.check('tb_fixed_generic_pkg.vhd')

    def test_function_generic_in_package(self):
        self.check('tb_function_generic_in_package.vhd')

    def test_generics_in_packages(self):
        self.check('tb_generics_in_packages.vhd')

    def test_type_generics_in_packages(self):
        self.check('tb_type_generics_in_packages.vhd')

    def test_psl(self):
        self.check('tb_psl.vhd')

    def check(self, testbench_name):
        vu = VUnit.from_argv(['--clean'])
        lib = vu.add_library('lib')
        lib.add_source_files(join(dirname(__file__), testbench_name))
        self.assertTrue(vu._main(), 'Failing test case(s) in testbench')

if __name__ == '__main__':
    unittest.main()
