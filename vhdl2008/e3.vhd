-- Generic types in entity
library ieee;
use ieee.std_logic_1164.all;
entity e3 is
	generic(
		type mytype
	);
	port(
		data     : in  mytype;
		data_out : out mytype
	);
end entity;

architecture RTL of e3 is
begin
	assert ?? '1' report "'??' is not supported" severity note;
end architecture RTL;
