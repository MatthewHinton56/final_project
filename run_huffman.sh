#!/bin/bash

#configs=($(grep "^class" /work2/07996/befoxwor/maverick2/final_project/configs/GPU_config_huffman.py | cut -d ' ' -f2 | sed 's/()://'))
configs=($(grep "^class" /work2/07996/befoxwor/maverick2/final_project/configs/GPU_config_v100.py | cut -d ' ' -f2 | sed 's/()://'))

for c in ${configs[@]}; do
        python sim.py \
                /work2/07996/befoxwor/maverick2/rodinia_3.1/cuda/huffman \
                $c \
                /work2/07996/befoxwor/maverick2/rodinia_3.1/data/huffman/test1024_H2.206587175259.in 
done
