# See LICENSE.iitm for details
# See LICENSE.vyoma for details
"""__________________________________Both Self and Linear Checking TestBench________________________________________"""
import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 
####################################################################################################################
################################____Self_Checking_TestBench_Method1____#############################################
####################################################################################################################

"""
Instructions
ORN    : 0b01000000000000000110000000110011
RORI   : 0b01100000000000000101000000010011
SROI   : 0b00100000000000000101000000010011
XNORN  : 0b01000000000000000100000000110011
SLO    : 0b00100000000000000001000000110011
SRO    : 0b00100000000000000101000000110011
ROL    : 0b01100000000000000001000000110011
ROR    : 0b01100000000000000101000000110011
SBCLR  : 0b01001000000000000001000000110011
SBSET  : 0b00101000000000000001000000110011
SBINV  : 0b01101000000000000001000000110011
SBEXT  : 0b01001000000000000101000000110011
GORC   : 0b00101000000000000101000000110011
GREV   : 0b01101000000000000101000000110011
SLOI   : 0b00100000000000000001000000010011
SBCLRI : 0b01001000000000000001000000010011
SBSETI : 0b00101000000000000001000000010011
SBINVI : 0b01101000000000000001000000010011
SBEXTI : 0b01001000000000000101000000010011
GORCI  : 0b00101000000000000101000000010011
GREVI  : 0b01101000000000000101000000010011
CMIX   : 0b00000110000000000001000000110011
CMOV   : 0b00000110000000000101000000110011
FSL    : 0b00000100000000000001000000110011
FSR    : 0b00000100000000000101000000110011
FSRI   : 0b00000100000000000101000000010011

ANDN   : 0b01000000000000000111000000110011
"""
"""
list_ins = [0b01000000000000000110000000110011,0b01100000000000000101000000010011,0b00100000000000000101000000010011,
            0b01000000000000000100000000110011,0b00100000000000000001000000110011,0b00100000000000000101000000110011,
            0b01100000000000000001000000110011,0b01100000000000000101000000110011,0b01001000000000000001000000110011,
            0b00101000000000000001000000110011,0b01101000000000000001000000110011,0b01001000000000000101000000110011,
            0b00101000000000000101000000110011,0b01101000000000000101000000110011,0b00100000000000000001000000010011,
            0b01001000000000000001000000010011,0b00101000000000000001000000010011,0b01101000000000000001000000010011,
            0b01001000000000000101000000010011,0b00101000000000000101000000010011,0b01101000000000000101000000010011,
            0b00000110000000000001000000110011,0b00000110000000000101000000110011,0b00000100000000000001000000110011,
            0b00000100000000000101000000110011,0b00000100000000000101000000010011,0b01000000000000000111000000110011]

@cocotb.test()
def run_test_SAMPLE_EXAMPLE(dut):
    for i in list_ins:
        # clock
        cocotb.fork(clock_gen(dut.CLK))

        # reset
        dut.RST_N.value <= 0
        yield Timer(10) 
        dut.RST_N.value <= 1

        ######### CTB : Modify the test to expose the bug #############
        # input transaction
        mav_putvalue_src1 = 0xABCDEF11
        mav_putvalue_src2 = 0x11ABCDEF
        mav_putvalue_src3 = 0x1ABCDEF1
        mav_putvalue_instr = i

        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

        dut._log.info("instruction = %s",dut.mav_putvalue_instr.value)
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'            
        assert dut_output == expected_mav_putvalue, error_message

"""  
"""
####################################################################################################################
################################____Self_Checking_TestBench_Method2____#############################################
####################################################################################################################


list_ins = [0b01000000000000000110000000110011,0b01100000000000000101000000010011,0b00100000000000000101000000010011,
            0b01000000000000000100000000110011,0b00100000000000000001000000110011,0b00100000000000000101000000110011,
            0b01100000000000000001000000110011,0b01100000000000000101000000110011,0b01001000000000000001000000110011,
            0b00101000000000000001000000110011,0b01101000000000000001000000110011,0b01001000000000000101000000110011,
            0b00101000000000000101000000110011,0b01101000000000000101000000110011,0b00100000000000000001000000010011,
            0b01001000000000000001000000010011,0b00101000000000000001000000010011,0b01101000000000000001000000010011,
            0b01001000000000000101000000010011,0b00101000000000000101000000010011,0b01101000000000000101000000010011,
            0b00000110000000000001000000110011,0b00000110000000000101000000110011,0b00000100000000000001000000110011,
            0b00000100000000000101000000110011,0b00000100000000000101000000010011,0b01000000000000000111000000110011]

@cocotb.test()
def run_test_SAMPLE_EXAMPLE(dut):
    for i in list_ins:
        # clock
        cocotb.fork(clock_gen(dut.CLK))



        # reset
        dut.RST_N.value <= 0
        yield Timer(10) 
        dut.RST_N.value <= 1

        mav_putvalue_instr = i

        p = 0x11111100 # For full range put p = 0x00000000 and q = 0xFFFFFFFF
        q = 0x111111FF

        for r in range (p,q):
            for s in range (p,q):
                mav_putvalue_src1 = s
                mav_putvalue_src2 = r
                mav_putvalue_src3 = 0x0
        

                # expected output from the model
                expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

                # driving the input transaction
                dut.mav_putvalue_src1.value = mav_putvalue_src1
                dut.mav_putvalue_src2.value = mav_putvalue_src2
                dut.mav_putvalue_src3.value = mav_putvalue_src3
                dut.EN_mav_putvalue.value = 1
                dut.mav_putvalue_instr.value = mav_putvalue_instr
  
                yield Timer(1) 

                # obtaining the output
                dut_output = dut.mav_putvalue.value

                cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
                cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
                cocotb.log.info(f'DUT SRC1={hex(mav_putvalue_src1)}')
                cocotb.log.info(f'DUT SRC2={hex(mav_putvalue_src2)}')

                dut._log.info("instruction = %s",dut.mav_putvalue_instr.value)
                error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'            
                assert dut_output == expected_mav_putvalue, error_message
""" 

####################################################################################################################
################################__Linear_Checking_TestBench____#####################################################
####################################################################################################################
"""
# Sample Test
@cocotb.test()
def run_test_SAMPLE_EXAMPLE(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x101010B3

    print(type(mav_putvalue_instr))

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    print(type(dut_output))
    print(type(expected_mav_putvalue))

    dut._log.info("instruction = %s",dut.mav_putvalue_instr.value)
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message



@cocotb.test()
#________________________________________ORN____________________________________________________
def run_test_ORN(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0b00000000000000000000000000000011
    mav_putvalue_src3 = 0b11111111111111111110000000011111
    mav_putvalue_instr =0b01000000000000000110000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 


@cocotb.test()
#________________________________________ANDN____________________________________________________
def run_test_ANDN(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b00000000000000001010101010100000
    mav_putvalue_src2 = 0b00000000000000000000000000000011
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01000000000000000111000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 


@cocotb.test()
#________________________________________XNOR____________________________________________________
def run_test_XNOR(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0b11111111111111111110000000011111
    mav_putvalue_src3 = 0b00000000000000000000000010101011
    mav_putvalue_instr =0b01000000000000000100000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 



@cocotb.test()
#________________________________________SLO____________________________________________________
def run_test_SLO(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b00000011110000001010100000000011
    mav_putvalue_src2 = 0b11111111111111111110000000011111
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b00100000000000000001000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 


@cocotb.test()
#________________________________________SRO____________________________________________________
def run_test_SRO(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b11000101111001011111111111111111
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b00100000000000000101000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 



@cocotb.test()
#________________________________________ROL____________________________________________________
def run_test_ROL(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b11000101111001011111111111111111
    mav_putvalue_src2 = 0b01100000000000000001000000110011
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01100000000000000001000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 


@cocotb.test()
#________________________________________ROR____________________________________________________
def run_test_ROR(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b01100000000000000001000000110011
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01100000000000000101000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________SBCLR____________________________________________________
def run_test_SBCLR(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b00000000000000000000000000000011
    mav_putvalue_src2 = 0b11111111111111111111111111111111
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01001000000000000001000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________SBSET____________________________________________________
def run_test_SBSET(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0b00000100111010100000000000000011
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b00101000000000000001000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________SBINV____________________________________________________
def run_test_SBINV(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b00000100111010100000000000000011
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01101000000000000001000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________SBEXT____________________________________________________
def run_test_SBEXT(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b01001000000000000101000000110011
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01001000000000000101000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________GORC____________________________________________________
def run_test_GORC(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0b01001000000000000101000000110011
    mav_putvalue_src2 = 0x1011Ba10
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b00101000000000000101000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________GREV____________________________________________________
def run_test_GREV(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x010100A0
    mav_putvalue_src2 = 0x1011BA10
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01101000000000000101000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________SLOI____________________________________________________
def run_test_SLOI(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x010100A0
    mav_putvalue_src2 = 0x1011BA10
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b00100000000000000001000000010011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________SROI____________________________________________________
def run_test_SROI(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0xFF0100A0
    mav_putvalue_src2 = 0x1CDFBA10
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b00100000000000000101000000010011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message 

@cocotb.test()
#________________________________________RORI____________________________________________________
def run_test_RORI(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0xF
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01100000000000000101000000010011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 



    # obtaining the output
    dut_output = dut.mav_putvalue.value

    
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
