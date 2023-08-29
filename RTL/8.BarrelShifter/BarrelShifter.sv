// Code your design here
module barrel_shifter
  (
    input logic [1:0]c,
    input logic [3:0] din,
    output logic [3:0] y
  
  );
  
  always_comb
    begin
      unique case(c)
        2'b00 : y = din;
        2'b01 : y = {din[0],din[3:1] };
        2'b10 : y = {din[1],din[0], din[3:2] };
        2'b11 : y = {din[2],din[1], din[0], din[3] };
      endcase
    end
endmodule