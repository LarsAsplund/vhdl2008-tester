vhdl2008-tester
===============

`run_test.py` is a script for testing to what extent your simulator can handle VHDL 2008. All testbenches located in the `vhdl2008` directory are based on the [VUnit test framework](http://vunit.github.io) which you must [install](http://vunit.github.io/installing.html) to run the test. You will also need Python and a simulator supported by VUnit which you can find information about [here](http://vunit.github.io/about.html).

You run the script like this (if Python is on your path)

``` console
python run_test.py
```

and a typical test result may look like this (snippet)

``` console
======================================================================
ERROR: test_entity_generic_type (__main__.TestVHDL2008Support)
----------------------------------------------------------------------
...
vunit.exceptions.CompileError: Failed to compile 'd:\Programming\github\vhdl2008-tester\vhdl2008\tb_entity_generic_type.vhd'

======================================================================
ERROR: test_psl (__main__.TestVHDL2008Support)
----------------------------------------------------------------------
...
vunit.exceptions.CompileError: Failed to compile 'd:\Programming\github\vhdl2008-tester\vhdl2008\tb_psl.vhd'

======================================================================
FAIL: test_matching_operator (__main__.TestVHDL2008Support)
----------------------------------------------------------------------
...
AssertionError: False is not true : Failing test case(s) in testbench

----------------------------------------------------------------------
Ran 9 tests in 74.329s

FAILED (failures=1, errors=2)
```

The first two testbenches (`test_entity_generic_type` and `test_psl`) failed with a compilation error since the simulator used in the example doesn't understand the tested VHDL 2008 syntax. The last testbench (`test_matching_operator`) compiled and simulated but not all VHDL test cases passed. If you look at the preceeding output you can get more details.

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
fail lib.tb_matching_operators.Testing matching equality between values with different drive strength   (0.3 seconds)
fail lib.tb_matching_operators.Testing matching equality with -                                         (0.3 seconds)
fail lib.tb_matching_operators.Testing matching equality with X                                         (0.5 seconds)
fail lib.tb_matching_operators.Testing matching equality with W                                         (0.3 seconds)
fail lib.tb_matching_operators.Testing matching equality with Z                                         (0.3 seconds)
fail lib.tb_matching_operators.Test matching inequality between same values                             (0.3 seconds)
fail lib.tb_matching_operators.Test matching inequality between different values                        (0.3 seconds)
fail lib.tb_matching_operators.Testing matching inequality between values with different drive strength (0.3 seconds)
fail lib.tb_matching_operators.Testing matching inequality with -                                       (0.3 seconds)
fail lib.tb_matching_operators.Testing matching inequality with X                                       (0.3 seconds)
fail lib.tb_matching_operators.Testing matching inequality with W                                       (0.3 seconds)
fail lib.tb_matching_operators.Testing matching inequality with Z                                       (0.3 seconds)
fail lib.tb_matching_operators.Test matching less than between same values                              (0.3 seconds)
fail lib.tb_matching_operators.Test matching less than between a low and a high value                   (0.3 seconds)
fail lib.tb_matching_operators.Test matching less than between a high and a low value                   (0.3 seconds)
fail lib.tb_matching_operators.Testing matching less than between weak values                           (0.3 seconds)
fail lib.tb_matching_operators.Testing matching less than with X                                        (0.3 seconds)
fail lib.tb_matching_operators.Test matching less than or equal between same values                     (0.3 seconds)
fail lib.tb_matching_operators.Test matching less than or equal between a low and a high value          (0.3 seconds)
fail lib.tb_matching_operators.Test matching less than or equal a between high and a low value          (0.3 seconds)
fail lib.tb_matching_operators.Testing matching less than or equal between weak values                  (0.3 seconds)
fail lib.tb_matching_operators.Testing matching less than or equal with X                               (0.3 seconds)
fail lib.tb_matching_operators.Test matching greater than between same values                           (0.3 seconds)
fail lib.tb_matching_operators.Test matching greater than between a low and a high value                (0.3 seconds)
fail lib.tb_matching_operators.Test matching greater than between a high and a low value                (0.3 seconds)
fail lib.tb_matching_operators.Testing matching greater than between weak values                        (0.3 seconds)
fail lib.tb_matching_operators.Testing matching greater than with W                                     (0.5 seconds)
fail lib.tb_matching_operators.Testing matching greater than with Z                                     (0.3 seconds)
fail lib.tb_matching_operators.Testing matching greater than with U                                     (0.3 seconds)
fail lib.tb_matching_operators.Test matching greater than or equal between same values                  (0.3 seconds)
fail lib.tb_matching_operators.Test matching greater than or equal between a low and a high value       (0.3 seconds)
fail lib.tb_matching_operators.Test matching greater than or equal a between high and a low value       (0.3 seconds)
fail lib.tb_matching_operators.Testing matching greater than or equal between weak values               (0.3 seconds)
fail lib.tb_matching_operators.Testing matching greater than or equal with W                            (0.5 seconds)
fail lib.tb_matching_operators.Testing matching greater than or equal with Z                            (0.3 seconds)
fail lib.tb_matching_operators.Testing matching greater than or equal with U                            (0.3 seconds)
===========================================================================================================================
pass 10 of 48
fail 38 of 48
===========================================================================================================================
```

This is not at all a complete test suite for VHDL 2008 but something to get started. Please suggest or provide more tests. 