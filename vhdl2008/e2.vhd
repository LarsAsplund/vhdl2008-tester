-- Operator ??
library ieee;
use ieee.std_logic_1164.all;
entity e2 is
end entity;

architecture RTL of e2 is
	
begin
	assert ?? '1' report "'??' is not supported" severity note;
end architecture RTL;
