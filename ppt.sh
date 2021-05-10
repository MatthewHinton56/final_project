#/bin/bash
ptx_file=$1
target_kernel=$2
loop_iteration=$3
target_gpu=$4
cd ./PPT/code/apps/PPT-GPU/
task_list=$(python PTXParser.py ../../../../$ptx_file $target_kernel $loop_iteration $target_gpu)
#echo $task_list
num_register=$5
static_shared_mem=$6
phit_l2=$7
block_size=$8
grid_size=$9
config="${10}"
python gpu_sim.py $num_register $static_shared_mem $phit_l2 $block_size $grid_size "$task_list" $config
cat perf.0.out
