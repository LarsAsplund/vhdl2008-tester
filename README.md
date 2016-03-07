vhdl2008-tester
===============

`run_test.py` is a script for testing to what extent your simulator can handle VHDL 2008. All testbenches located in the `testbenches` directory are based on the [VUnit test framework](http://vunit.github.io) which you must [install](http://vunit.github.io/installing.html) to run the test. You will also need Python and a simulator supported by VUnit which you can find information about [here](http://vunit.github.io/about.html).

You run the script like this (if Python is on your path)

``` console
python run_test.py
```

and a typical test result may look like this (snippet)

``` console
======================================================================
FAIL: test_entity_generic_type (__main__.TestVHDL2008Support)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_test.py", line 33, in test_entity_generic_type
    self.check('tb_entity_generic_type')
  File "run_test.py", line 52, in check
    self.assertEqual(retcode, 0)
AssertionError: 1 != 0

======================================================================
FAIL: test_matching_operator (__main__.TestVHDL2008Support)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_test.py", line 9, in test_matching_operator
    self.check('tb_matching_operator')
  File "run_test.py", line 52, in check
    self.assertEqual(retcode, 0)
AssertionError: 1 != 0

======================================================================
FAIL: test_psl (__main__.TestVHDL2008Support)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_test.py", line 27, in test_psl
    self.check('tb_psl')
  File "run_test.py", line 52, in check
    self.assertEqual(retcode, 0)
AssertionError: 1 != 0

----------------------------------------------------------------------
Ran 10 tests in 88.783s

FAILED (failures=3)
```

Testbenches may fail because of compilation errors when the VHDL 2008 syntax isn't understood or it may fail because of a failing test case within a testbench. You will find the details in the preceding output but you can also rerun just the failing test. To rerun the first test above you do

``` console
python run_test.py TestVHDL2008Support.test_entity_generic_type
```

In this case we have a compilation error (snippet)

``` console
Compiling d:\Programming\github\vhdl2008-tester\testbenches\tb_entity_generic_type\tb_entity_generic_type.vhd into lib ...
** Error: d:\Programming\github\vhdl2008-tester\testbenches\tb_entity_generic_type\tb_entity_generic_type.vhd(4): (vcom-1440) Language feature INTERFACE TYPES IN ENTITY DECLARATIONS is not supported yet.
```

The second failing test compiles but then there are failing test cases (snippet)

``` console
==== Summary ==============================================================================================================
pass lib.tb_matching_operators.Testing matching equality with U                                         (0.3 seconds)
pass lib.tb_matching_operators.Testing matching inequality with U                                       (0.3 seconds)
pass lib.tb_matching_operators.Testing matching less than with W                                        (0.3 seconds)
pass lib.tb_matching_operators.Testing matching less than with Z                                        (0.3 seconds)
pass lib.tb_matching_operators.Testing matching less than with U                                        (0.3 seconds)
pass lib.tb_matching_operators.Testing matching less than or equal with W                               (0.3 seconds)
pass lib.tb_matching_operators.Testing matching less than or equal with Z                               (0.3 seconds)
pass lib.tb_matching_operators.Testing matching less than or equal with U                               (0.3 seconds)
pass lib.tb_matching_operators.Testing matching greater than with X                                     (0.3 seconds)
pass lib.tb_matching_operators.Testing matching greater than or equal with X                            (0.3 seconds)
fail lib.tb_matching_operators.Test matching equality between same values                               (0.8 seconds)
fail lib.tb_matching_operators.Test matching equality between different values                          (0.5 seconds)

...

fail lib.tb_matching_operators.Testing matching greater than or equal with U                            (0.3 seconds)
===========================================================================================================================
pass 10 of 48
fail 38 of 48
===========================================================================================================================
```

To study these problems more closely you can launch that testbench in your simulator by running the associated VUnit run script which is located under `testbenches\<name of testbench>`. In this case

```
> cd testbenches\tb_matching_operator
> python run.py --gui *"matching equality between same values"*
```

will launch the GUI of my simulator with the first failing test case such that it can be debugged. Type `python run.py -h` to see what else you can do with the VUnit run script.

This is not at all a complete test suite for VHDL 2008 but something to get started. Please suggest or provide more tests. 