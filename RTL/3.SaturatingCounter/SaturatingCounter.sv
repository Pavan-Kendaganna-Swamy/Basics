module counter (
  input logic [7:0] data_in,
  input logic clk, mode,
  output logic [7:0] data_out
  
  
);
  
  logic [7:0] temp;
  
  always_ff @(posedge clk)
    begin
      if(mode)
        begin
          temp <= (8'b11111111 )? (8'b11111111 ) :data_in + 1;
        end
      else  
        begin
          temp <= 8'b0 ? 8'b0 : data_in -1;
        end 
    end
 assign dout = temp; 
endmodule