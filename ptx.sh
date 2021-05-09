#/bin/bash
input=$1
/opt/apps/cuda/11.0/bin/nvcc --ptx $input
ptx="$(basename $input .cu).ptx"
echo $ptx
OUTPUT=$(cat $ptx | grep ".visible .entry" | tr -d '()')
for word in $OUTPUT
do
  if [[ $word != .* ]]
  then
    echo $word  
  fi
done
