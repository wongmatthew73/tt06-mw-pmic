`default_nettype none

module pmic(
    input clk,
    input reset,
    //input enable,
    input busy,
    input [7:0] adcVoltage,
    output convStart,
    output rd_cs,
    output syncRectifierLs,
    output syncRectifierHs
    );
    
    wire slowerClk;
    
    slow_clk slowClk(
    	.original_clk(clk), 
    	.reset(reset), 
    	.slow_clk(slowerClk)
    	);
    pwm syncPWM(
    	.clk(slowerClk), 
    	.reset(reset), 
    	//.enable(enable), 
    	.busy(busy), 
    	.adcVoltage(adcVoltage), 
    	.convStart(convStart), 
    	.rd_cs(rd_cs),
    	.syncRegOutLs(syncRectifierLs),
    	.syncRegOutHs(syncRectifierHs)
    	);
  
    
endmodule

