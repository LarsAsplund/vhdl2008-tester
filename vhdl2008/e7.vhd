-- Protected type
package e7 is
	type shared_counter is protected
		procedure reset;
		procedure increment(by : integer := 1);
		impure function value return integer;
	end protected shared_counter;
end package;