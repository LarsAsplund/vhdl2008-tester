-- PSL
library ieee;
use ieee.std_logic_1164.all;

entity e8 is
	port (
		clk : in std_logic;
		rst : in std_logic;
		req : in std_logic;
		ack : in std_logic
	);
end entity;
architecture RTL of e8 is
	
begin
	assert always req -> next[2] (grant); -- is this correct?
end architecture;
