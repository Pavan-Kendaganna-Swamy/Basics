module full_adder (
	input logic a,b,c,
  output logic sum,carry
  
  
);
  
  always_comb
    begin
      assign sum = (a ^ b ^ c);
      assign carry = c&((a ^ b) + (a & b));
    end

endmodule 