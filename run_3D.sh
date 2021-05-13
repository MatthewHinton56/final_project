#!/bin/bash

configs=($(grep "^class" configs/GPU_config_hotspot3D.py | cut -d ' ' -f2 | sed 's/()://'))

for c in ${configs[@]}; do
	python sim_3D.py \
		$WORK2/final_project/rodinia_3.1/cuda/hotspot3D \
		$c \
		512 8 100 \
		$WORK2/final_project/rodinia_3.1/data/hotspot3D/power_512x8 \
		$WORK2/final_project/rodinia_3.1/data/hotspot3D/temp_512x8 \
		output.out
done
