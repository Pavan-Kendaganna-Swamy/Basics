module half_adder (
	input logic a,b,
  output logic sum,carry
  
  
);
  
  always_comb
    begin
      assign sum = (a ^ b);
      assign carry = (a & b);
    end

endmodule  