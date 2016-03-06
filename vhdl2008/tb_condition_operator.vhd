library vunit_lib;
context vunit_lib.vunit_context;

library ieee;
use ieee.std_logic_1164.all;
entity tb_condition_operator is
  generic (
    runner_cfg : runner_cfg_t);
end entity;

architecture tb of tb_condition_operator is
begin
  test_runner: process is
  begin
    test_runner_setup(runner, runner_cfg);

    while test_suite loop
      if run("Test condition operator with 1") then
        check_equal(?? std_logic'('1'), true);
        check_equal(?? bit'('1'), true);
      elsif run("Test condition operator with H") then
        check_equal(?? 'H', true);
      elsif run("Test condition operator with 0") then
        check_equal(?? std_logic'('0'), false);
        check_equal(?? bit'('0'), false);
      elsif run("Test condition operator with L") then
        check_equal(?? 'L', false);
      elsif run("Test condition operator with U") then
        check_equal(?? 'U', false);
      elsif run("Test condition operator with W") then
        check_equal(?? 'W', false);
      elsif run("Test condition operator with X") then
        check_equal(?? 'X', false);
      elsif run("Test condition operator with Z") then
        check_equal(?? 'Z', false);
      elsif run("Test condition operator with -") then
        check_equal(?? '-', false);

      end if;
    end loop;

    test_runner_cleanup(runner);
    wait;
  end process test_runner;
end architecture tb;
