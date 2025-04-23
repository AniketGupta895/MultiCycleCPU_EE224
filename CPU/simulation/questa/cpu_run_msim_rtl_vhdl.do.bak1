transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/SE9_16.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/SE6_16.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/register_file.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/reg.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/pad_lli.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/n_bit_register.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/n_bit_or.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/n_bit_inverter.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/n_bit_imply.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/n_bit_and.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/mux16bit8to1.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/mux16bit4to1.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/mux16bit2to1.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/mux8x1.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/mux3bit4to1.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/memory.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/LHI.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/instruction_register.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/full_adder.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/demux1x8.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/ConditionCodeRegister.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/n_bit_full_adder.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/n_bit_adder_subtractor.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/four_bit_multiplier.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/alu.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/datapath.vhd}
vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/fsm.vhd}

vcom -93 -work work {C:/quartus_projects/EE214/project/CPU/fsm_tb.vhd}

vsim -t 1ps -L altera -L lpm -L sgate -L altera_mf -L altera_lnsim -L fiftyfivenm -L rtl_work -L work -voptargs="+acc"  fsm_tb

add wave *
view structure
view signals
run -all
