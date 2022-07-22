# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge


@cocotb.test()
async def test_seq_bug1_1011(dut):
    # test for input 1011 __________________________________________________________________
    

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut._log.info("current_state after applying reset = %s ",dut.current_state.value)
   
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)

    assert dut.seq_seen.value == 1 , f"sequence is incorrectly detected {dut.seq_seen.value} != 1"


@cocotb.test()
async def test_seq_bug1_11011(dut):

    # test for 11011 ____________________________________________________________________________
   
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock 

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    dut._log.info("current_state after applying reset = %s ",dut.current_state.value)

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 1 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 11 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 110 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 1101 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 11011 current_state = %s ",dut.current_state.value)
   
    assert dut.seq_seen.value == 1 , f"sequence is incorrectly detected {dut.seq_seen.value} != 1"


@cocotb.test()
async def test_seq_bug1_1001011(dut):
    # test for input 1001011 ______________________________________________________________________
   
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock 

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    dut._log.info("current_state after applying reset = %s ",dut.current_state.value)

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 1 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 10 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 100 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 1001 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 10010 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 100101 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 1001011 current_state = %s ",dut.current_state.value)
   
    assert dut.seq_seen.value == 1 , f"sequence is incorrectly detected {dut.seq_seen.value} != 1"



@cocotb.test()
async def test_seq_bug1_10111011(dut):
    # test for input 10111011 __________________________________________________________________
    

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)

    

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0   
    await FallingEdge(dut.clk)

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)
       

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    assert dut.seq_seen.value == 1 , f"sequence is incorrectly detected {dut.seq_seen.value} != 1"

@cocotb.test()
async def test_seq_bug1_101011(dut):
    # test for input 101011 ________________________________________________________________
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock 

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    dut._log.info("current_state after applying reset = %s ",dut.current_state.value)

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 1 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 10 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 101 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 1010 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 10101 current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("after receiving 101011 current_state = %s ",dut.current_state.value)
   
    assert dut.seq_seen.value == 1 , f"sequence is present but not detected {dut.seq_seen.value} != 1"

@cocotb.test()
async def test_seq_bug1_001011(dut):
    # test for input 001011 __________________________________________________________________
    

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut._log.info("current_state after applying reset = %s ",dut.current_state.value)
   
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)

    assert dut.seq_seen.value == 1 , f"sequence is incorrectly detected {dut.seq_seen.value} != 1"




@cocotb.test()
async def test_seq_bug1_1011011(dut):
    #test for input 1011011 ____________________________________________________________________
   
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock 

    dut._log.info("current_state before applying reset = %s ",dut.current_state.value)

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    dut._log.info("current_state after applying reset = %s ",dut.current_state.value)

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info("current_state = %s ",dut.current_state.value)
    assert dut.seq_seen.value == 1 , f"sequence is incorrectly detected {dut.seq_seen.value} != 1"

