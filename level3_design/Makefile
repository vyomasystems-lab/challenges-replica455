# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/FIFO_BUFFER_MEMORY.v              # provide your design path

TOPLEVEL := FIFO_BUFFER_MEMORY         # design file
MODULE   := MY_TEST     # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
