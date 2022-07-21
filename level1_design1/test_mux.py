# See LICENSE.vyoma for details
import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_0(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = random.randint(0,3)
    dut.sel.value = 0
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp0.value, f"mux result incorrect: {dut.inp0.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_1(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp1.value = random.randint(0,3)
    dut.sel.value = 1
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp1.value, f"mux result incorrect: {dut.inp1.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_2(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp2.value = random.randint(0,3)
    dut.sel.value = 2
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp2.value, f"mux result incorrect: {dut.inp2.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_3(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp3.value = random.randint(0,3)
    dut.sel.value = 3
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp3.value, f"mux result incorrect: {dut.inp3.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_4(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp4.value = random.randint(0,3)
    dut.sel.value = 4
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp4.value, f"mux result incorrect: {dut.inp4.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_5(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp5.value = random.randint(0,3)
    dut.sel.value = 5
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp5.value, f"mux result incorrect: {dut.inp5.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_6(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp6.value = random.randint(0,3)
    dut.sel.value = 6
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp6.value, f"mux result incorrect: {dut.inp6.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_7(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp7.value = random.randint(0,3)
    dut.sel.value = 7
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp7.value, f"mux result incorrect: {dut.inp7.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_8(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp8.value = random.randint(0,3)
    dut.sel.value = 8
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp8.value, f"mux result incorrect: {dut.inp8.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_9(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp9.value = random.randint(0,3)
    dut.sel.value = 9
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp9.value, f"mux result incorrect: {dut.inp9.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_10(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp10.value = random.randint(0,3)
    dut.sel.value = 10
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp10.value, f"mux result incorrect: {dut.inp10.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_11(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp11.value = random.randint(0,3)
    dut.sel.value = 11
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp11.value, f"mux result incorrect: {dut.inp11.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_12(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp12.value = 2
    dut.sel.value = 12
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp12.value, f"mux result incorrect: {dut.inp12.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_13(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp13.value = 3
    dut.sel.value = 13
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp13.value, f"mux result incorrect: {dut.inp13.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_14(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp14.value = random.randint(0,3)
    dut.sel.value = 14
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp14.value, f"mux result incorrect: {dut.inp14.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_15(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp15.value = random.randint(0,3)
    dut.sel.value = 15
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp15.value, f"mux result incorrect: {dut.inp15.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_16(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp16.value = random.randint(0,3)
    dut.sel.value = 16
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp16.value, f"mux result incorrect: {dut.inp16.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_17(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp17.value = random.randint(0,3)
    dut.sel.value = 17
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp17.value, f"mux result incorrect: {dut.inp17.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_18(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp18.value = random.randint(0,3)
    dut.sel.value = 18
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp18.value, f"mux result incorrect: {dut.inp18.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_19(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp19.value = random.randint(0,3)
    dut.sel.value = 19
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp19.value, f"mux result incorrect: {dut.inp19.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_20(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp20.value = random.randint(0,3)
    dut.sel.value = 20
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp20.value, f"mux result incorrect: {dut.inp20.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_21(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp21.value = random.randint(0,3)
    dut.sel.value = 21
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp21.value, f"mux result incorrect: {dut.inp21.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_22(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp22.value = random.randint(0,3)
    dut.sel.value = 22
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp22.value, f"mux result incorrect: {dut.inp22.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_23(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp23.value = random.randint(0,3)
    dut.sel.value = 23
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp23.value, f"mux result incorrect: {dut.inp23.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_24(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp24.value = random.randint(0,3)
    dut.sel.value = 24
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp24.value, f"mux result incorrect: {dut.inp24.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_25(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp25.value = random.randint(0,3)
    dut.sel.value = 25
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp25.value, f"mux result incorrect: {dut.inp25.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_26(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp26.value = random.randint(0,3)
    dut.sel.value = 26
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp26.value, f"mux result incorrect: {dut.inp26.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_27(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp27.value = random.randint(0,3)
    dut.sel.value = 27
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp27.value, f"mux result incorrect: {dut.inp27.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_28(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp28.value = random.randint(0,3)
    dut.sel.value = 28
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp28.value, f"mux result incorrect: {dut.inp28.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_29(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp29.value = random.randint(0,3)
    dut.sel.value = 29
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp29.value, f"mux result incorrect: {dut.inp29.value}!={dut.out.value}"
@cocotb.test()
async def test_mux_30(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp30.value = 1
    dut.sel.value = 30
    await Timer(1,units='ns')
    assert dut.out.value==dut.inp30.value, f"mux result incorrect: {dut.inp30.value}!={dut.out.value}"




