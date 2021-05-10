"""
*********** Performance Prediction Toolkit PPT *********

File: gpu_app.py
Description: The application which is to run on the accelerator (GPU)
Author: Yehia Arafa 
"""

# Set up path  variables; PPT applications expect it in this fashion.
from sys import path
import sys
path.append('../..')
from ppt import *
path.append('configs/')
import string
from GPU_config import *

import nodes


task_list=[]
num_register = 0 # Number of registers available for the applcation
static_shared_mem = 0 # Static shared memory available for the application 
phit_l2 = 0.0 #--> Estimation from real device <loads & stores>
block_size = 0
grid_size = 0
config = ''


############################
# Simian Engine parameters #
############################

simName, startTime, endTime, minDelay = "perf", 0.0, 1000000.0, 0.000001
simianEngine = Simian(simName, startTime, endTime, minDelay)


#############################################
# The application to run on the modeled GPU #
#############################################


def app(this, arg, *args): #Rodinia->Gaussain 
	'''
	We are simulating only the kernel call and not taking into account the CPU to GPU memory allocation and byte transfered transfer.
	This will added for the CPU+GPU version. 
	'''
	node = this.entity
	core = node.cores[0]
	vector_size = 1024
 
	print (task_list)
	print (block_size)
	print (grid_size)
	print (num_register)
	print (static_shared_mem)
	print (phit_l2) 
   

	GPU_tasklist = [['KERNEL_CALL', 0, task_list, block_size, grid_size, num_register, static_shared_mem, phit_l2]]
	core.time_compute(GPU_tasklist, simianEngine.now, True)


######################################################################################
# The Handler which have the application's tasklist and the target config GPU inside #
######################################################################################

def GPU_APP_Handler(self, msg, *args):
	print ('Config: ' + config)
	self.createProcess("app", app)
	gpu_config = get_gpu_config(getattr(sys.modules[__name__], config)) #K40m is one of the classes in [configs/GPU_config]
	self.generate_target_accelerator(gpu_config)
	self.startProcess("app", self) 


if __name__ == "__main__":
	'''
	For now, we choose to have a node (GPUNode) that have only one accelerator with a dummy host (GPUCore) 
	and an interconnect (cielo_intercon)
	''' 
	num_register = eval(sys.argv[1])
	static_shared_mem = eval(sys.argv[2])
	phit_l2 = eval(sys.argv[3])
	block_size = eval(sys.argv[4])
	grid_size = eval(sys.argv[5])
	task_list = eval(sys.argv[6])
	config = sys.argv[7]
  
	modeldict = { 
            "model_name"    : "n01",
            "sim_time"      : 1000000,
            "use_mpi"       : False,
            "intercon_type" : "Bypass",
            "torus"         : configs.cielo_intercon,
            "host_type"     : "CieloNode",
            "load_libraries": set(["mpi"]),
            "mpiopt"        : configs.gemini_mpiopt,
            "debug_options" : []
            } 
    
    #########
    # STEPS #
    #########

    # 1. Add a compute node to the engine
	simianEngine.addEntity("Node", nodes.GPUNode, 0, modeldict, 1,1,1,1,1,1,1,1,1,1)

    # 2. Create a new GPU_APP Service on the node
	simianEngine.attachService(nodes.Node, "GPU_APP_Handler" , GPU_APP_Handler)
	
    # 3. Scheduling the GPU_APP service to run at time 0 
	simianEngine.schedService(0, "GPU_APP_Handler", None, "Node", 0)
 
    # 4. Run simian
	simianEngine.run()

    # 5. Exit simian
	simianEngine.exit()
