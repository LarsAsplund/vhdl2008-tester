import unittest
from subprocess import call
import sys
from os import environ
from os.path import join, dirname

class TestVHDL2008Support(unittest.TestCase):
    def test_matching_operator(self):
        self.check('tb_matching_operator')

    def test_condition_operator(self):
        self.check('tb_condition_operator')

    def test_fixed_generic_pkg(self):
        self.check('tb_fixed_generic_pkg')

    def test_function_generic_in_package(self):
        self.check('tb_function_generic_in_package')

    def test_generics_in_packages(self):
        self.check('tb_generics_in_packages')

    def test_type_generics_in_packages(self):
        self.check('tb_type_generics_in_packages')

    def test_psl(self):
        self.check('tb_psl')

    def test_numeric_std_unsigned(self):
        self.check('tb_numeric_std_unsigned')

    def test_entity_generic_type(self):
        self.check('tb_entity_generic_type')

    def test_bit_string_literals(self):
        self.check('tb_bit_string_literals')

    def setUp(self):
        self.output_path = join(dirname(__file__), "run_test_out")
        self.report_file = join(self.output_path, "xunit.xml")
        self.testbench_root = join(dirname(__file__), 'testbenches')

    def check(self, testbench_name):
        new_env = environ.copy()
        new_env["VUNIT_VHDL_STANDARD"] = '2008'
        run_file = join(self.testbench_root, testbench_name, 'run.py')
        retcode = call([sys.executable, run_file,
                        "--clean",
                        "--output-path=%s" % self.output_path,
                        "--xunit-xml=%s" % self.report_file],
                       env=new_env)
        self.assertEqual(retcode, 0)

if __name__ == '__main__':
    unittest.main()
