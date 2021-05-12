import sys
import os
from sys import path
path.append('configs/')
from GPU_config import *
from PTXParser import *
from gpu_sim import *
path.append('../..')
from ppt import *
from subprocess import PIPE, STDOUT, Popen, check_call

cu_directory = sys.argv[1]
config_selection = sys.argv[2]

kernels = {}
num_registers = 12
static_shared_memory = 4

def find_kernel_and_file(kernel):
    for ptx_file in kernels:
      for ptx_kernel in kernels[ptx_file]:
        if kernel in ptx_kernel:
            return (ptx_file, ptx_kernel)

def simulate_kernel(kernel, loop_iterations, config, block_size, grid_size, phit_l2):
    ptx_file, ptx_kernel = find_kernel_and_file(kernel)
    print(ptx_file + ' ' + ptx_kernel)
    gpu_config = get_gpu_config(getattr(sys.modules[__name__], config))
    print(config + ' ' + gpu_config["gpu_arch"])
    task_list = ptx_parse_function(ptx_file, ptx_kernel, loop_iterations, gpu_config["gpu_arch"])
    #simulate_gpu( num_registers, static_shared_memory, phit_l2, block_size, grid_size, task_list, config, gpu_config)
    proc = Popen(['python', 'gpu_sim.py', str(num_registers), str(static_shared_memory), str(phit_l2), str(block_size), str(grid_size), str(task_list), config], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #print(out)
    #print(err)
    #print (task_list)
    output = {}
    perf = open('perf.0.out')
    for line in perf:
        #print(line)
        if 'Overall IPC' in line:
            output['IPC'] = eval(line.split()[2][:-1])
        if 'Total GPU computations took' in line:
            output['Time'] = eval(line.split()[4])
        if 'Overall MIPS' in line:
            output['MIPS'] = eval(line.split()[2][:-1])
    perf.close()
    check_call(['rm', 'perf.0.out'])
    return output
    

def build_kernel_map(ptx_file):
    #print(ptx_file)
    kernels[ptx_file] = []
    f = open(ptx_file, 'r')
    for line in f:
        if '.entry' in line:
            if '.visible' in line:        
                kernels[ptx_file] += [line.split()[2].replace('(', '')]
            else: 
                kernels[ptx_file] += [line.split()[1].replace('(', '')]
    #print(kernels[ptx_file])


for root, dirs, files in os.walk(cu_directory):
    for file in files:
        if file.endswith(".cu"):
             #print(os.path.join(root, file))
             check_call(['/opt/apps/cuda/11.0/bin/nvcc', '--ptx', os.path.join(root, file)], stdout=PIPE, stderr=STDOUT)
             #os.system('/opt/apps/cuda/11.0/bin/nvcc --ptx ' + os.path.join(root, file))
             ptx_file = file.replace('.cu', '.ptx')
             build_kernel_map(ptx_file)
         
input_file = sys.argv[3] 
file_size = os.path.getsize(input_file)
num_elements = (file_size // 4) 
num_threads_per_block = 256
num_blocks = num_elements // num_threads_per_block
iterations = int(math.log(num_threads_per_block, 2.0))
#print(config_selection)
#for config in config_selection:
  #print(config)
print (str(simulate_kernel('vlc_encode_kernel_sm64huff', [4, iterations], config_selection, num_threads_per_block, num_blocks, .5)))