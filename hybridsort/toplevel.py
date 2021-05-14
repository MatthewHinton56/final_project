import os
import sys
from subprocess import PIPE, STDOUT, Popen, check_call
SIZE = 1048576
DIVISIONS = 1024
config = sys.argv[1]
thread_scale = sys.argv[2]
#os.system('python sim_histogram1024Kernel.py ../../../../rodinia_3.1/cuda/hybridsort/ G1080TI ' + str(SIZE))
proc = Popen(['python', 'sim_histogram1024Kernel.py', '../../../../rodinia_3.1/cuda/hybridsort/', config, str(SIZE), thread_scale], stdout=PIPE, stderr=PIPE)
kernel = 1
out, err = proc.communicate()
#print(out)
print(err) 

ipc = 0
time = 0
mips = 0

histogram_ipc = 0
histogram_time = 0
histograme_mips = 0

perf = open('perf.0.out')
for line in perf:
    if 'Overall IPC' in line:
        histogram_ipc = eval(line.split()[2][:-1])
    if 'Total GPU computations took' in line:
        histogram_time = eval(line.split()[4])
    if 'Overall MIPS' in line:
        histograme_mips = eval(line.split()[2][:-1])
perf.close()

print('histogram ipc: ' + str(histogram_ipc))
print('histogram time: ' + str(histogram_time))
print('histogram mips: ' + str(histograme_mips))

ipc += histogram_ipc
time += histogram_time
mips += histograme_mips

#os.system('python sim_bucketcount.py ../../../../rodinia_3.1/cuda/hybridsort/ G1080TI ' + str(SIZE) + ' ' + str(DIVISIONS))

proc = Popen(['python', 'sim_bucketcount.py', '../../../../rodinia_3.1/cuda/hybridsort/', config, str(SIZE), str(DIVISIONS), thread_scale], stdout=PIPE, stderr=PIPE)
out, err = proc.communicate()
#print(out)
print(err) 
kernel += 1

bucket_ipc = 0
bucket_time = 0
bucket_mips = 0

perf = open('perf.0.out')
for line in perf:
    #print(line)
    if 'Overall IPC' in line:
        bucket_ipc += eval(line.split()[2][:-1])
    if 'Total GPU computations took' in line:
        bucket_time += eval(line.split()[4])
    if 'Overall MIPS' in line:
        bucket_mips += eval(line.split()[2][:-1])
perf.close()
#print(output)

#os.system('python sim_bucketprefixoffset.py ../../../../rodinia_3.1/cuda/hybridsort/ G1080TI ' + str(SIZE) + ' ' + str(DIVISIONS))

proc = Popen(['python', 'sim_bucketprefixoffset.py', '../../../../rodinia_3.1/cuda/hybridsort/', config, str(SIZE), str(DIVISIONS), thread_scale], stdout=PIPE, stderr=PIPE)
out, err = proc.communicate()
#print(out)
print(err) 
kernel += 1

perf = open('perf.0.out')
for line in perf:
    #print(line)
    if 'Overall IPC' in line:
        bucket_ipc += eval(line.split()[2][:-1])
    if 'Total GPU computations took' in line:
        bucket_time += eval(line.split()[4])
    if 'Overall MIPS' in line:
        bucket_mips += eval(line.split()[2][:-1])
perf.close()

#os.system('python sim_bucketsort.py ../../../../rodinia_3.1/cuda/hybridsort/ G1080TI ' + str(SIZE) + ' ' + str(DIVISIONS))

proc = Popen(['python', 'sim_bucketsort.py', '../../../../rodinia_3.1/cuda/hybridsort/', config, str(SIZE), str(DIVISIONS), thread_scale], stdout=PIPE, stderr=PIPE)
out, err = proc.communicate()
#print(out)
print(err)
kernel += 1

perf = open('perf.0.out')
for line in perf:
    if 'Overall IPC' in line:
        bucket_ipc += eval(line.split()[2][:-1])
    if 'Total GPU computations took' in line:
        bucket_time += eval(line.split()[4])
    if 'Overall MIPS' in line:
        bucket_mips += eval(line.split()[2][:-1])
perf.close()

print('bucket ipc: ' + str(bucket_ipc / 3))
print('bucket time: ' + str(bucket_time / 3))
print('bucket mips: ' + str(bucket_mips / 3))

ipc += bucket_ipc
time += bucket_time
mips += bucket_mips

merge_ipc = 0
merge_time = 0
merge_mips = 0

#os.system('python sim_mergeSortFirst.py ../../../../rodinia_3.1/cuda/hybridsort/ G1080TI ' + str(SIZE))

proc = Popen(['python', 'sim_mergeSortFirst.py', '../../../../rodinia_3.1/cuda/hybridsort/', config, str(SIZE), thread_scale], stdout=PIPE, stderr=PIPE)
out, err = proc.communicate()
#print(out)
print(err)
kernel += 1
perf = open('perf.0.out')
for line in perf:
    if 'Overall IPC' in line:
        merge_ipc += eval(line.split()[2][:-1])
    if 'Total GPU computations took' in line:
        merge_time += eval(line.split()[4])
    if 'Overall MIPS' in line:
        merge_mips += eval(line.split()[2][:-1])
perf.close()


nrElems = 2;
largestSize = SIZE / DIVISIONS
while True:
    floatsperthread = (nrElems*4)
    threadsPerDiv = int(largestSize/floatsperthread) 
    threadsNeeded = threadsPerDiv * DIVISIONS
    threads = 208 
    blocks = threadsNeeded/threads if ((threadsNeeded%threads) == 0) else (threadsNeeded/threads) + 1
    if blocks < 8:
        blocks = 8
        threads = threadsNeeded / blocks if ((threadsNeeded%blocks) == 0) else (threadsNeeded / blocks) + 1


    #os.system('python sim_mergeSortPass.py ../../../../rodinia_3.1/cuda/hybridsort/ G1080TI ' + str(nrElems) + ' ' + str(threads) + ' ' + str(blocks))
    kernel += 1
    proc = Popen(['python', 'sim_mergeSortPass.py', '../../../../rodinia_3.1/cuda/hybridsort/', config, str(nrElems), str(threads), str(blocks), thread_scale], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    #print(out)
    print(err)
    #print ('file')
    perf = open('perf.0.out')
    for line in perf:
        #print ('line: ' + line)
        if 'Overall IPC' in line:
            merge_ipc += eval(line.split()[2][:-1])
        if 'Total GPU computations took' in line:
            merge_time += eval(line.split()[4])
        if 'Overall MIPS' in line:
            merge_mips += eval(line.split()[2][:-1])
    perf.close()
    nrElems *= 2
    floatsperthread = (nrElems*4)
    if threadsPerDiv == 1: 
        break


proc = Popen(['python', 'sim_mergepack.py', '../../../../rodinia_3.1/cuda/hybridsort/', config, str(SIZE), str(DIVISIONS), thread_scale], stdout=PIPE, stderr=PIPE)
out, err = proc.communicate()
#print(out)
print(err)

perf = open('perf.0.out')
for line in perf:
    if 'Overall IPC' in line:
        merge_ipc += eval(line.split()[2][:-1])
    if 'Total GPU computations took' in line:
        merge_time += eval(line.split()[4])
    if 'Overall MIPS' in line:
        merge_mips += eval(line.split()[2][:-1])
perf.close()
kernel += 1

ipc +=  merge_ipc
time += merge_time
mips += merge_mips

print('merge ipc: ' + str(merge_ipc / (kernel - 4)))
print('merge time: ' + str(merge_time / (kernel - 4)))
print('merge mips: ' + str(merge_mips / (kernel - 4)))


print('ipc: ' + str(ipc / kernel))
print('mips: ' + str(mips / kernel))
print('time: ' + str(time))

#os.system('python sim.py ../../../../rodinia_3.1/cuda/huffman/ G1080TI ../../../../rodinia_3.1/data/huffman/test1024_H2.206587175259.in')