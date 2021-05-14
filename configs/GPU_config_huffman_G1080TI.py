"""
*********** Performance Prediction Toolkit PPT *********

File: GPU_config.py
Description: Target GPU configurations
Author: Yehia Arafa 
"""

import sys 
from arch_latencies_config import *



def get_gpu_config(gpu):
    new_gpu = gpu()
    config = new_gpu.populate_config()
    return config


class G1080TI():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))
       
        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 
        
        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6	    # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9	    # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3 		# Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]
        
        config["warp_size"]                  = 32		    # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64		    # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32		    # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024		    # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048		    # Max number of threads queued or active on a single SM
        
        config["global_mem_return_queue"]    = 128		    # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1L2M2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]*2
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]*2
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1L2D2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]/2
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]/2
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1L2D4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]/4
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]/4
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1L2D8():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]/8
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]/8
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_RM2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536*2      # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_RM3():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536*3      # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_RM4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536*4      # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_SMM2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]*2

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_SMM4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]*4

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_SMD2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]/2

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_SMD4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]/4

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1M2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]*2
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1M4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]*4
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1D2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]/2
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L1D4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]/4
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L2M2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]*2
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L2M4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]*4
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L2D2():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]/2
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class G1080TI_L2D4():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "G1080TI"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 28           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor   
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor  
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor 
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1481*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 

        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 2.75*10**6           # L2 cache size in Bytes
        config["global_mem_size"]            = 11*10**9     # Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3                 # Shared memory size in Bytes per multiprocessor  

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]/4
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32                   # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64                   # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32                   # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024                 # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048                 # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128                  # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config

