-- Matching Operators
library ieee;
use ieee.std_logic_1164.all;
entity e1 is
end entity e1;

architecture RTL of e1 is
begin
	assert '1' ?=  'H' report "'?= ' is not supported" severity note;
	assert 'L' ?/= 'H' report "'?/=' is not supported" severity note;
	assert 'L' ?<  'H' report "'?< ' is not supported" severity note;
	assert '1' ?<= 'H' report "'?<=' is not supported" severity note;
	assert '1' ?>  'H' report "'?> ' is not supported" severity note;
	assert '1' ?>= 'H' report "'?>=' is not supported" severity note;
end architecture RTL;
