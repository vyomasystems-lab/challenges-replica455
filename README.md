# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ___Level1_design1 Verification___ 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
### MUX Verification 

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![Verification L1D1 Mux](https://user-images.githubusercontent.com/55652905/180143753-509b5dc2-b6a0-4643-be51-438925c8e7fc.JPG)

# Verification Environment

The CoCoTb based Python test is developed as explained.The test drives inputs to the Design Under Test (mux module here) which takes in 31 (each 2 bit) inpus (inp0 to inp30) and depending on the 5 bit select (sel) only one input is transmitted to 2 bit output (out).

1. ___The values 2 assigned to the input pin 12 (inp12 = 2) and corresponding select as 12 (sel = 12)___

```
dut.inp12.value = 2
dut.sel.value = 12
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.out.value==dut.inp12.value, f"mux result incorrect: {dut.inp12.value}!={dut.out.value}"
AssertionError: mux result incorrect: 10!=00
```
2. ___The values 3 assigned to the input pin 13 (inp13 = 3) and corresponding select as 13 (sel = 13)___

```
dut.inp13.value = 3
dut.sel.value = 13
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.out.value==dut.inp13.value, f"mux result incorrect: {dut.inp13.value}!={dut.out.value}"
AssertionError: mux result incorrect: 11!=10
```
3. ___The values 1 assigned to the input pin 30 (inp30 = 1) and corresponding select as 30 (sel = 30)___

```
dut.inp30.value = 1
dut.sel.value = 30
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.out.value==dut.inp30.value, f"mux result incorrect: {dut.inp30.value}!={dut.out.value}"
AssertionError: mux result incorrect: 01!=00
```

# Test Scenario

![L1D1](https://user-images.githubusercontent.com/55652905/180151639-ea6c7df7-a287-4044-b892-a45cc06e2ec5.JPG)

Output(out) mismatches for the above inputs proving that there are design bugs

# Design Bug

Based on the above test input and analysing the design, we see the following


```
begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;  ==> BUG 1- It will be "5'b01100" instead of "5'b01101"
      5'b01101: out = inp13;  ==> BUG 2- It will automatically get corrected because of previous bug 
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
                               ==> BUG 3- "5'b11110: out = inp30" is missing
      default: out = 0;
    endcase
  end
```

![L1D1 report](https://user-images.githubusercontent.com/55652905/180153540-0e6039e0-f645-40ae-9932-ec925d52d4c1.JPG)




# Design Fix

Updating the design and re-running the test makes the test pass.

![L1D1 corrected](https://user-images.githubusercontent.com/55652905/180154479-d5b3e80b-1926-4ba6-8647-e9b934147b34.JPG)

# Verification Strategy

The test bench was produced considering all the possible values of select line (sel) from 00000 (0) to 11110 (30) which selects the corresponding inputs from inp0 to inp30. At first all the input pins are made to set random values from 0 to 3 to ensure 2 bit inputs. After running the test it was observed trat 12 ,13 and 30 has failed. To ensure they failed random inputs in input pin 12 13 and 30 was removed and made fixed values to 2 , 3 and 1 respectively. the test still failed. After debugging I ran the test for 15 times a row and all the test "Passed"

# Is the verification complete ?

Yes the verification complete, All the test passed even in multiple times of running the python test bench, keeping in mind all the possible input combination has been checked generating the expected output results.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ___Level1_design2 Verification___
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
### 1011 Pattern detector verification


The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![pattern detector](https://user-images.githubusercontent.com/55652905/180365748-ce900c1e-07aa-401a-af53-5901f8e4494c.JPG)

# Verification Environment

The CoCoTb based Python test is developed as explained.The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes in 1 bit input sequence (inp_bit), 1 bit reset , clock signal and produce output of high logic whenever complete "1011" sequence is encountered in the input bit 

1. ___The sequence 101011 is applied to the input pin (inp_bit) ___

```
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1 , f"sequence is present but not detected {dut.seq_seen.value} != 1"
AssertionError: sequence is present but not detected 0 != 1
```

2. ___The sequence 11011 is applied to the input pin (inp_bit) ___

```
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1 , f"sequence is present but not detected {dut.seq_seen.value} != 1"
AssertionError: sequence is present but not detected 0 != 1
```

3. ___The sequence 1011011 is applied to the input pin (inp_bit) ___

```
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1 , f"sequence is present but not detected {dut.seq_seen.value} != 1"
AssertionError: sequence is present but not detected 0 != 1
```

4. ___The sequence 10111011 is applied to the input pin (inp_bit) ___

```
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1 , f"sequence is present but not detected {dut.seq_seen.value} != 1"
AssertionError: sequence is present but not detected 0 != 1
```

# Test Scenario


![table](https://user-images.githubusercontent.com/55652905/180376388-6164add8-cdc7-41f3-87b8-9e6baf770135.JPG)

Output(seq_seen) mismatches for the above inputs proving that there are design bugs.

# Design Bug

Based on the above test input and analysing the design, we see the following

```
  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;   // ==> 1 Bug - failing to detect 11011
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;  
        else
          next_state = IDLE;  // ==> 1 Bug - failing to detect 101011
      end
      SEQ_1011:
      begin
        next_state = IDLE;  // ==> 2 Bug - failing to detect 10111011 and 1011011
      end
    endcase
  end
endmodule
```

![10111011](https://user-images.githubusercontent.com/55652905/180379945-814a0646-06bf-4f6e-bc18-846fca72be3f.JPG)
![11011](https://user-images.githubusercontent.com/55652905/180379955-2e800828-64bd-4703-a976-43547df877a3.JPG)
![101011](https://user-images.githubusercontent.com/55652905/180379957-76357a31-28ec-4889-a46c-4a896571c32e.JPG)
![1011011](https://user-images.githubusercontent.com/55652905/180379963-556b89b2-2cc5-4d83-a5f6-ef70afaaf058.JPG)

# Design Fix


![WhatsApp Image 2022-07-22 at 12 48 27 PM](https://user-images.githubusercontent.com/55652905/180385467-c8a1fcde-6cf7-4f87-a1e4-70f77b77c92d.jpeg)

Updating the verilog design according to new state diagram.

```
// See LICENSE.vyoma for more details
// Verilog module for Sequence detection: 1011
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
      
    end
    else
    begin
      current_state <= next_state;

    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1; // <-- for detecting 11011 ...
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;   
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_10;  // <-- specially for detecting 101011 ...
      end
      SEQ_1011:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1; // <--specially for detecting 10111011 ...
        else
          next_state = SEQ_10; // <-- specially for detecting 1011011 ...
      end
    endcase
  end
endmodule

```

Rerunning all the test-


![allpass](https://user-images.githubusercontent.com/55652905/180380818-d77a6656-877e-4958-b861-890cc0550558.JPG)


# Verification Strategy

First of all I made the State graph flow considering the buggy design and then the test bench was produced considering all the critical possible values of input sequence bit i.e. inp_bit {1011, 10111011, 1011011, 101011, 1001011, 11011, 001011} consisting of overlapping and non-overlapping sequence. Upon failing a test I revisitted the State graph and modifies the graph flow and also the verilog code logic corosponding to the graph modified graph. After failing consecutive 4 test and modifying the graph flow and verilog code I finally arrive the point where all the test cases passed  

# Is the verification complete ?

Yes the verification complete because the design is capturing all the overlapping and non-overlapping 1011 sequrnce and rejecting all other sequence.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ___Level2_design Verification___
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
### Bit Manupulation coprocessor

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![processor](https://user-images.githubusercontent.com/55652905/180694971-916dcc69-4b12-4bfd-bfd5-52d04edd86ef.JPG)


# Verification Environment

The CoCoTb based Python test is developed as explained.The test drives inputs to the Design Under Test (mux module here) which takes in 31 (each 2 bit) inpus (inp0 to inp30) and depending on the 5 bit select (sel) only one input is transmitted to 2 bit output (out).

1. ___The ANDN operation___

```
 # input transaction
    mav_putvalue_src1 = 0b00000000000000001010101010100000
    mav_putvalue_src2 = 0b00000000000000000000000000000011
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr =0b01000000000000000111000000110011
```
The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut_output == expected_mav_putvalue, error_message
AssertionError: Value mismatch DUT = 0x1 does not match MODEL = 0x15541
```

# Test Scenario 

1. ANDN Operation
- Test Inputs: 
1.   src1=0b00000000000000001010101010100000 
2.  src2=0b00000000000000000000000000000011
3. src3=0x0
4.  instr=0b01000000000000000111000000110011.
- Expected Output: EXPECTED OUTPUT=0x15541
- Observed Output: DUT OUTPUT=0x1


# Verification Strategy

Particularly for Self chacking test bench(method 1) I made a list of instructions for verification and conducted the test imside the for loop so that each and every instructions added in the list are called for execution. Then in self checking test bench (method 2) I went further to provide a range of hexadecimal inputs. For a mear range of 00 to FF it took about 20 min. for the test. for range 00000000 to FFFFFFFF it will take eternity. Then there was Linear check which was quite simple. manually providing each and every instructions and inputs.

# Is the verification complete ?

Yes the verification complete, A wide range of test has been conducted out of which only 1 bug is detected.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ___Level3_design Verification___
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
### Synchronous FIFO buffer memory

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![pass22](https://user-images.githubusercontent.com/55652905/180923357-ae16928f-b4af-4cc0-be17-1cc278c64804.JPG)

# Verification Environment

The CoCoTb based Python test is developed as explained. 
- Test1: Underflow Test=> With no input at data_in we try to read the output and observe the "empty" signal respense
- Test2: Input_DataStorage_and_empty_signal_response_test=> We feed some input value and observe the Stored value 
                                                          using read operation and then check the atatus of "empty"
                                                          signal
- Test3:Input_to_memory_storage_to_output_test_and_Fifo_Operation_test => Like previous test we store the input to 
                                                                        but also observe the FIFO operation i.e. 
                                                                        if the oldest data is getting replaced with
                                                                        newly inserted data. We also use "assert" 
                                                                        check if the data stored in memory is the data
                                                                        we are getting as output through Data_out pin
- Test4:Input_to_output_test_test=> We are not conserned in observing the data storage operation. Here we treat the 
                                  whole DUT as black box and using "assert" check we check the input applied
                                  and output obtained from DUT i.e. data_in == data_out
                                  
1. Test 3 Failed :

```
- dut.data_in.value  = 00000000000000000000000000111011
```          
Obviously during Write operation we made write and enable signal high and reset signal low 
The assert statement is used for comparing the stored value of memory amd the output received in output pin (port)
During the read operation we made the read signal high
The following error is seen:

```
assert dut.memory[i].value == dut.data_out.value, f"Output Signal is Incorrect: {dut.memory[i].value}!=0 {dut.data_out.value}"
AssertionError: Output Signal is Incorrect: 00000000000000000000000000111011!= 00000000000000000000000001000010
```
![fail1](https://user-images.githubusercontent.com/55652905/180925044-04ce5b66-417b-42d4-9311-529f3290fd37.JPG)

2. Test 4 Failed :

```
- dut.data_in.value  = 01110110001011100010101001110001
```    
Obviously during Write operation we made write and enable signal high and reset signal low 
The assert statement is used for comparing the input value at input pin to the observed data available at the output pin
During the read operation we made the read signal high
The following error is seen:

```
assert dut.data_in.value == dut.data_out.value , f"Output Empty Signal is Incorrect: {dut.data_in.value}!={dut.data_out.value}"
AssertionError: Output Empty Signal is Incorrect: 01110110001011100010101001110001!=10101100001100010101110110110001
```
![Fail2](https://user-images.githubusercontent.com/55652905/180925927-64ea80ad-54a2-4001-a4a1-7ba8dfa5ea8b.JPG)


# Test Scenario

### Test 3 :
- Input:                00000000000000000000000000111011
- Expected Output :     00000000000000000000000000111011
- Observed DUT Output : 00000000000000000000000001000010

### Test 4 :
- Input:                01110110001011100010101001110001
- Expected Output :     01110110001011100010101001110001
- Observed DUT Output : 10101100001100010101110110110001

Output mismatches for the above inputs proving that there are design bugs.

# Design Bug

Based on the above test input and analysing the design, we see the following

```
always @ (posedge clock) 
begin 
 if (enable==0); //if "Active High Enable" condition is low then do nothing
 else begin 
  if (reset) begin 
   read_pointer = 0; 
   write_pointer = 0; 
  end 
  else if (read ==1'b1 && count!=0) begin 
   data_out  = memory[read_pointer]; 
                                         //<== BUG : Read pointer is not incrementing; Missing : read_pointer = read_pointer+1;
  end 
  else if (write==1'b1 && count<8) begin
   memory[write_pointer]  = data_in; 
   write_pointer  = write_pointer+1; 
  end 
  else; 
 end 
//Error Handeling of read and write pointer
 if (write_pointer==8) 
  write_pointer=0; 
 else if (read_pointer==8) 
  read_pointer=0; 
 else;
// Adjusting the "count" value for function of "EMPTY"
 if (read_pointer > write_pointer) begin 
  count=read_pointer-write_pointer; 
 end 
 else if (write_pointer > read_pointer) 
  count=write_pointer-read_pointer; 
 else;
end 

endmodule 
```

# Design Fix 

```
always @ (posedge clock) 
begin 
 if (enable==0); //if "Active High Enable" condition is low then do nothing
 else begin 
  if (reset) begin 
   read_pointer = 0; 
   write_pointer = 0; 
  end 
  else if (read ==1'b1 && count!=0) begin 
   data_out  = memory[read_pointer]; 
   read_pointer = read_pointer+1;     //<== Fixed 
  end 
  else if (write==1'b1 && count<8) begin
   memory[write_pointer]  = data_in; 
   write_pointer  = write_pointer+1; 
  end 
  else; 
 end 
//Error Handeling of read and write pointer
 if (write_pointer==8) 
  write_pointer=0; 
 else if (read_pointer==8) 
  read_pointer=0; 
 else;
// Adjusting the "count" value for function of "EMPTY"
 if (read_pointer > write_pointer) begin 
  count=read_pointer-write_pointer; 
 end 
 else if (write_pointer > read_pointer) 
  count=write_pointer-read_pointer; 
 else;
end 

endmodule 
```
Rerunning all the 4 test 

![pass22](https://user-images.githubusercontent.com/55652905/180927830-d55c377d-b723-44ce-95fc-7c397003b4cd.JPG)
![pass11](https://user-images.githubusercontent.com/55652905/180927843-8805c049-e49d-432a-8a2a-40175dfcc1d9.JPG)
![pass1](https://user-images.githubusercontent.com/55652905/180927864-0cfef392-9c91-4060-ba79-d7d49694de35.JPG)
![pass2](https://user-images.githubusercontent.com/55652905/180927888-6fdfb943-899b-485f-b7ff-ed6969e92da9.JPG)

# Verification Strategy

For test 1 we just have the read operation. For test 2 we apply inputs using for loop and randomized from 0 to 101 just for test, here we also print the stored memory value so that we can check manually if the input applied values are stored properly in the memory location. Test 3 we almost do the same thing but here we are interested to observe the content of memory locations and the value opserved at output pin , but side by side we also observe the FIFO action is performed properly or not by printing the value manually. For test 4 we apply the data input value and assert the data output. 

# Is the verification complete ?

Yes the verification complete, All the required test has been conducted with 2^32 input combinations and also proper memory storing, and FIFO action has been checked. Overall 1 bug has been detected.






