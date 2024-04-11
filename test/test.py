# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout
import random
#from encoder import Encoder

#Look into this number
clocks_per_phase = 10

async def reset(dut):
    dut.adcVoltage.value = 0
    dut.busy.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1;
    await ClockCycles(dut.clk, 5) # how long to wait for the debouncers to clear

#async def run_encoder_test(encoder, max_count):
    #for i in range(clocks_per_phase * 2 * max_count):
    #    await encoder.update(1)

   # # let noisy transition finish, otherwise can get an extra count
   # for i in range(10):
    #    await encoder.update(0)
        

@cocotb.test()
async def test_all(dut):
    clock = Clock(dut.clk, 10, units="us")

    cocotb.start_soon(clock.start())

    await reset(dut)
    await ClockCycles(dut.clk, 1)
    dut.adcVoltage.value = 0x05
    await ClockCycles(dut.clk, 1)


    #await with_timeout(FallingEdge(dut.convStart), 1000, 'ms')
    await FallingEdge(dut.convStart)
    await ClockCycles(dut.clk, 2)
    dut.busy.value = 1
    await ClockCycles(dut.clk, 10)
    dut.busy.value = 0
    
    #await with_timeout(FallingEdge(dut.convStart), 1000, 'ms')
    await FallingEdge(dut.convStart)
    dut.adcVoltage.value = 0xbb
    await ClockCycles(dut.clk, 2)
    dut.busy.value = 1
    await ClockCycles(dut.clk, 10)
    dut.busy.value = 0
    
    #await with_timeout(FallingEdge(dut.convStart), 1000, 'ms')
    await FallingEdge(dut.convStart)
    dut.adcVoltage.value = 0xff
    await ClockCycles(dut.clk, 2)
    dut.busy.value = 1
    await ClockCycles(dut.clk, 10)
    dut.busy.value = 0
    
    #await with_timeout(FallingEdge(dut.convStart), 1000, 'ms')
    await FallingEdge(dut.convStart)
    dut.adcVoltage.value = 0x33
    await ClockCycles(dut.clk, 2)
    dut.busy.value = 1
    await ClockCycles(dut.clk, 10)
    dut.busy.value = 0
    
    #await adcConversion(dut)
   

    # do 3 ramps for each encoder 
    max_count = 16384

    # pwm should all be on for max_count 
    for i in range(max_count): 
        await ClockCycles(dut.clk, 1)
        
        
