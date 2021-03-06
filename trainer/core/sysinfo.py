"""
记录计算机信息

这是一个控制台程序，会接收参数

由父进程调用，并且父进程可以杀死该子进程

"""

import os
import pynvml # pip install nvidia-ml-py3
import psutil 
import time 
import argparse

from trainer.core.msmg import MessageManager


def run_sysinfo_subprocess(trainName):
    """ 在py子进程获取机器信息"""
    import subprocess

    pyFile = os.path.abspath(__file__)
    cmd = "python {pyFile} \"{trainName}\"".format(pyFile=pyFile,trainName=trainName)
    sysInfoSubprocess = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

    return sysInfoSubprocess


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("trainName", help="训练程序的名称或id")
    args = parser.parse_args()
    return args


def link_msmg(trainName):
    msMg = MessageManager()
    msMg.band_trainName(trainName)
    return msMg


def main(trainName):
    """"""

    print(trainName)
    if not isinstance(trainName,str):
        trainName = str(trainName)
    msMg = link_msmg(trainName)

    # 静态量

    cpuCount = psutil.cpu_count()
    memoryTotal = psutil.virtual_memory().total/1024/1024/1024 # G

    try:
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(1) # 0 是？ 1 是 1080Ti
        gpuMemoryTotal = pynvml.nvmlDeviceGetMemoryInfo(handle).total/1024/1024/1024 # G
        pynvml.nvmlShutdown()
    except:
        gpuMemoryTotal = None

    sleepTime = 60
    sendTimeStep = 60 # 60 step发送一次结果

    sysStaticInfoDict = {
        "cpuCount":cpuCount,
        "memoryTotal":"{memoryTotal} G".format(memoryTotal=memoryTotal),
        "gpuMemoryTotal":"{gpuMemoryTotal} G".format(gpuMemoryTotal = gpuMemoryTotal),
        "sleepTime":sleepTime,
        # "sendTimeStep":sendTimeStep
    }

    msMg.push(sysStaticInfoDict,topic="sysStaticInfoDict")


    # 动态量
    
    step = 0
    isStartFlag = True
    while True:
        
        # 
        net = psutil.net_io_counters()

        netRecv = net[1]
        netSent = net[0]

        # 
        disk = psutil.disk_io_counters()

        diskWrite = disk[1]
        diskRead = disk[0]

        if isStartFlag:

            oldNetRecv = netRecv
            oldNetSend = netSent
            oldDiskWrite = diskWrite
            oldDiskRead = diskRead
            time.sleep(sleepTime)
            isStartFlag = False
            continue

        #
        cpuPercent = psutil.cpu_percent()

        #
        memory = psutil.virtual_memory()
        memoryPercent = memory.percent

        # 

        netRecvPercent = (netRecv - oldNetRecv) / sleepTime / 1024 # kb/s 
        netSendPercent = (netSent - oldNetSend) / sleepTime / 1024 # kb/s 

        diskWritePercent = (diskWrite - oldDiskWrite) / sleepTime / 1024 # kb/s 
        diskReadPercent = (diskRead - oldDiskRead) / sleepTime / 1024 # kb/s 
        
        # 
        # if step % sendTimeStep == 0:
        sysIterInfoDict = {
            "step":step,
            "cpuPercent":cpuPercent,
            "memoryPercent":memoryPercent,
            "netRecvPercent":netRecvPercent,
            "netSendPercent":netSendPercent,
            "diskWritePercent":diskWritePercent,
            "diskReadPercent":diskReadPercent
        }

        msMg.push(sysIterInfoDict,topic="sysIterInfoDict")

        time.sleep(sleepTime)

        oldNetRecv = netRecv
        oldNetSend = netSent
        oldDiskWrite = diskWrite
        oldDiskRead = diskRead

        step += 1

        print(step)



if __name__ == "__main__":

    args = get_args()
    trainName = args.trainName
    main(trainName)

    

