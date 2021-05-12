#!/bin/bash

python sim.py \
	$WORK2/final_project/rodinia_3.1/cuda/hotspot3D \
	G1080TI \
	512 8 100 \
	$WORK2/final_project/rodinia_3.1/data/hotspot3D/power_512x8 \
	$WORK2/final_project/rodinia_3.1/data/hotspot3D/temp_512x8 \
	output.out
