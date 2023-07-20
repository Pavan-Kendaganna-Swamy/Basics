// Code your design here
module adder (
  input logic [3:0] A,B,C,D,
  input logic clk,
  output logic [5:0]dout
    
    
    
);

logic [4:0] temp1, temp2;
logic [4:0] q1, q2;
logic [5:0] temp3;
always_comb
begin
    temp1 = A +B;
    temp2 = C + D;
    temp3 = q1+q2;
end


always_ff@(posedge clk)
begin
    q1 <= temp1;
    q2<= temp2;
    dout <= temp3;
end


endmodule