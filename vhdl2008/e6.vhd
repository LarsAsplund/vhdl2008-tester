-- function generic and type generic for package
package e6 is
generic (
	type mytype;
	function inverse (x: mytype) return mytype
);
	
end package;