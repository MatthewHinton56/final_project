#/bin/bash
for config in V100 V100_sm2 V100_sm4 V100_sm8 V100_sm_half
do
  for thread_scale in .125 .25 .5 1 2
  do
    echo "$config"_"$thread_scale"
    python toplevel.py $config $thread_scale > "$config"_"$thread_scale".log
    #echo "test" > "$config"_"$thread_scale".log
  done
done 