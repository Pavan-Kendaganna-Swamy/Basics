// Code your design here
// Code your design here
module fsm
  (
    input logic data,clk, 
    output logic y
  );
  
  enum bit [1:0] {s1,s2,s3} current_state,next_state;
  //typdef state current_state,next_state
  
  
  
  always_ff@(posedge clk)
  begin
     current_state <= next_state;
   end
    
  
  always_comb
    begin
      case(current_state)
        
        s1:begin
          if(data)
            begin
            next_state = s2;
          	y =0;
            end
          else
            begin
            next_state = s1;
            y = 0;
            end
        end
        
        s2:begin
          
          if(!data)
            begin
            next_state = s3;
          	y =0;
            end
          else
            begin
            next_state = s2;
            y = 0;
            end
        end
        
        s3:begin
          
          if(data)
            begin
            next_state = s2;
          	y =1;
            end
          else
            begin
            next_state = s1;
            y = 0;
            end
        end
        
        
      endcase
    end

endmodule