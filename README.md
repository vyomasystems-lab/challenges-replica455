# ___Level1_design1 Verification___
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

# ___Level1_design2 Verification___

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






               



