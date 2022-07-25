import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import Timer

"""
Test1: Underflow Test=> With no input at data_in we try to read the output and observe the "empty" signal respense
Test2: Input_DataStorage_and_empty_signal_response_test=> We feed some input value and observe the Stored value 
                                                          using read operation and then check the atatus of "empty"
                                                          signal
Test3:Input_to_memory_storage_to_output_test_and_Fifo_Operation_test => Like previous test we store the input to 
                                                                        but also observe the FIFO operation i.e. 
                                                                        if the oldest data is getting replaced with
                                                                        newly inserted data. We also use "assert" 
                                                                        check if the data stored in memory is the data
                                                                        we are getting as output through Data_out pin
Test4:Input_to_output_test_test=> We are not conserned in observing the data storage operation. Here we treat the 
                                  whole DUT as black box and using "assert" check we check the input applied
                                  and output obtained from DUT i.e. data_in == data_out
"""

@cocotb.test()
async def Underflow_output_and_empty_signal_response_test(dut):
    ########## Underflow Test and Empty signal response ##############

    clock = Clock(dut.clock, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())

    value_read=0
    value_write=0
    value_enable=1
    value_reset=1

    dut.read.value = value_read
    dut.write.value = value_write
    dut.enable.value = value_enable
    dut.reset.value = value_reset

    await RisingEdge(dut.clock)

    value_reset = 0
    dut.reset.value = value_reset

    await RisingEdge(dut.clock)

    value_read = 1
    dut.read.value = value_read

    await RisingEdge(dut.clock)

    dut._log.info("Underflow test output = %s ", dut.data_out.value)

    assert dut.empty.value == 1, f"Output Empty Signal is Incorrect: {dut.empty.value}!=1"



@cocotb.test()
async def Input_DataStorage_and_empty_signal_response_test(dut):
    #____Testing for input to memory dasta storage and then observing the empty output signal response____

    dut._log.info("before test_3 read_pointer = %s  and write_pointer = %s", dut.read_pointer.value, dut.write_pointer.value)


    clock = Clock(dut.clock, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())

    value_read = 0
    value_write = 0
    value_enable = 1
    value_reset = 1

    dut.read.value = value_read
    dut.write.value = value_write
    dut.enable.value = value_enable
    dut.reset.value = value_reset

    await RisingEdge(dut.clock)

    value_reset = 0
    dut.reset.value = value_reset


    await RisingEdge(dut.clock)

    #inputs Writing
    for j in range (8):

        dut.write.value = 1
        dut.data_in.value = random.randint(1, 101)
        await RisingEdge(dut.clock)
        dut._log.info("in Write_pointer = %s, The input data is %s ", dut.write_pointer.value,dut.data_in.value) 
        
    dut.write.value = 0

    #Printing the Stored Menory value-
     
    for q in range (8):
        await RisingEdge(dut.clock)
        dut._log.info("stored value in memory[%s] = %s ",q, dut.memory[q].value)

    dut._log.info("after writing operation the value of read_pointer = %s  and write_pointer = %s", dut.read_pointer.value, dut.write_pointer.value)


    await RisingEdge(dut.clock)

    #Printing the Stored memory values using Read operation 

    for i in range(8):
        dut.read.value = 1
        await RisingEdge(dut.clock)
        dut._log.info("in read_pointer = %s memory value is memory[%s] = %s , ", dut.read_pointer.value,
                      dut.read_pointer.value, dut.memory[int(dut.read_pointer.value)].value)
        dut.read.value = 0
    dut._log.info("after reading operation the value of read_pointer = %s  and write_pointer = %s",
                  dut.read_pointer.value, dut.write_pointer.value)

    await RisingEdge(dut.clock)

    #Checking if the last output value is equal to last output value

    assert dut.data_in.value == dut.data_out.value, f"input vs output mapping is incorrect: {dut.data_in.value}!={dut.data_out.value}"

    #Checking the Empty signal response 

    assert dut.empty.value == 0, f"Output Empty Signal is Incorrect: {dut.empty.value}!=0"



@cocotb.test()
async def Input_to_memory_storage_to_output_test_and_Fifo_Operation_test(dut):
    #___ Observing the Input to memory storage to final output in data_out pin and also explaining the FIFO operation___

    dut._log.info("before test_3 read_pointer = %s  and write_pointer = %s", dut.read_pointer.value, dut.write_pointer.value)

    clock = Clock(dut.clock, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())

    value_read = 0
    value_write = 0
    value_enable = 1
    value_reset = 1

    dut.read.value = value_read
    dut.write.value = value_write
    dut.enable.value = value_enable
    dut.reset.value = value_reset

    await RisingEdge(dut.clock)

    value_reset = 0
    dut.reset.value = value_reset


    await RisingEdge(dut.clock)


    #inputs
    for j in range (12): #<----------------- range of iteration is made higher for explaining the fifo operation  

        dut.write.value = 1
        dut.data_in.value = random.randint(1, 101)
        await RisingEdge(dut.clock)
        dut._log.info("in Write_pointer = %s, The input data is %s ", dut.write_pointer.value,dut.data_in.value)

    dut.write.value = 0

    for q in range (8):
        await RisingEdge(dut.clock)
        dut._log.info("stored value in memory[%s] = %s ",q, dut.memory[q].value)

    dut._log.info("after writing operation the value of read_pointer = %s  and write_pointer = %s", dut.read_pointer.value, dut.write_pointer.value)


    await RisingEdge(dut.clock)

    for i in range(8):
        dut.read.value = 1
        await RisingEdge(dut.clock)
        dut._log.info("in read_pointer = %s memory value is memory[%s] = %s", dut.read_pointer.value,
                      dut.read_pointer.value, dut.memory[int(dut.read_pointer.value)].value)
        dut.read.value = 0
        await RisingEdge(dut.clock)
        dut._log.info("data out =%s", dut.data_out.value)
        assert dut.memory[i].value == dut.data_out.value, f"Output Empty Signal is Incorrect: {dut.memory[i].value}!=0 {dut.data_out.value}" #<----------------- output pin test


    dut._log.info("after reading operation the value of read_pointer = %s  and write_pointer = %s",
                  dut.read_pointer.value, dut.write_pointer.value)

    await RisingEdge(dut.clock)

    assert dut.empty.value == 0, f"Output Empty Signal is Incorrect: {dut.empty.value}!=0" #<--------------------- enable pin test



@cocotb.test()
async def Input_to_output_test_test(dut):
    #########Observing input pin to output pin#############


    clock = Clock(dut.clock, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())

    value_read = 0
    value_write = 0
    value_enable = 1


    dut.read.value = value_read
    dut.write.value = value_write
    dut.enable.value = value_enable


    await RisingEdge(dut.clock)
    dut.reset.value = 1
    await RisingEdge(dut.clock)
    dut.reset.value = 0
    await RisingEdge(dut.clock)

    for t in range (12):
        
        dut.write.value = 1
        dut.data_in.value = random.randint(1, 4294967296)
        await RisingEdge(dut.clock)
        dut.write.value = 0
        dut._log.info("DUT INPUT = %s",dut.data_in.value)
        dut.read.value = 1
        await RisingEdge(dut.clock) # Time to let the simulator to proceed
        dut.read.value = 0 
        await RisingEdge(dut.clock) # Time to storage 

        # From application of input to appropriate output it takes 2 clock cycle 

        dut._log.info("DUT OUT =   %s",dut.data_out.value)
        assert dut.data_in.value == dut.data_out.value , f"Output Empty Signal is Incorrect: {dut.data_in.value}!={dut.data_out.value}"
        

