#/bin/bash
config=$1
rodinia_test=$2
executable=$3
flags=$4
module load gcc/7.3
module load cuda/11.0
export CUDA_INSTALL_PATH=/opt/apps/cuda/11.0/
echo "$config"
echo "$rodinia_test"
cd ./gpgpu-sim_distribution
echo $PWD
source setup_environment
cd ..
cp -v $config/* $rodinia_test/
cd $rodinia_test
echo $PWD
make clean ; make
ldd $executable
echo $flags
./$executable $flags