module ICG
  (
    input logic clk, en, rst,
    output logic gclk
  );
  
  logic enl;
  

  
  always_latch
    begin
      if(rst)
      begin
        enl <= 0;
      end
      else if(!rst && !clk)
        begin
          enl <= en;
        end
      else
        begin
          enl <= enl;
        end
    end

  
  always_comb
    begin
      assign gclk = (enl && clk);
    end
  
  
endmodule