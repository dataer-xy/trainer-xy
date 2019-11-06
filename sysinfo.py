"""
记录计算机信息

这是一个控制台程序，会接收参数

由父进程调用，并且父进程可以杀死该子进程

"""


import pynvml # pip install nvidia-ml-py3
import psutil 
import time 
import argparse

from .msmg import MessageManager

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("trainName", required=True, type=str, help="训练程序的名称或id")
    args = parser.parse_args()
    return args


def main(trainName):
    """"""

    msMg = MessageManager()
    msMg.bind_projectName(trainName)

    # 静态量

    cpuCount = psutil.cpu_count()
    memoryTotal = psutil.virtual_memory().total/1024/1024/1024 # G

    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(1) # 0 是？ 1 是 1080Ti
    gpuMemoryTotal = pynvml.nvmlDeviceGetMemoryInfo(handle).total/1024/1024/1024 # G
    pynvml.nvmlShutdown()

    sysStaticInfo = {
        "cpuCount":cpuCount,
        "memoryTotal":memoryTotal,
        "gpuMemoryTotal":gpuMemoryTotal
    }

    msMg.push(sysStaticInfo,topic="sysStaticInfo")


    # 动态量
    sleepTime = 1

    isStartFlag = True
    while True:
        
        # 
        net = psutil.net_io_counters()

        netRecv = net[1]
        netSent = net[0]

        # 
        disk = psutil.disk_io_counters()

        diskRecv = disk[1]
        diskSent = disk[0]

        if isStartFlag:

            oldNetRecv = netRecv
            oldNetSend = netSent
            oldDiskRecv = diskRecv
            oldDiskSend = diskSent
            time.sleep(sleepTime)
            isStartFlag = False
            continue

        #
        cpuPercent = psutil.cpu_percent()

        #
        memory = psutil.virtual_memory()
        memoryPercent = memory.used / memory.total

        # 

        netRecvPercent = (netRecv - oldNetRecv) / 1024 # kb/s 
        netSendPercent = (netSent - oldNetSend) / 1024 # kb/s 

        diskRecvPercent = (diskRecv - oldDiskRecv) / 1024 # kb/s 
        diskSendPercent = (diskSent - oldDiskSend) / 1024 # kb/s 

        # 
        sysInfoDict = {
            "cpuPercent":cpuPercent,
            "memoryPercent":memoryPercent,
            "netRecvPercent":netRecvPercent,
            "netSendPercent":netSendPercent,
            "diskRecvPercent":diskRecvPercent,
            "diskSendPercent":diskSendPercent
        }

        msMg.push(sysInfoDict,topic="sysInfoDict")

        time.sleep(sleepTime)

        oldNetRecv = netRecv
        oldNetSend = netSent
        oldDiskRecv = diskRecv
        oldDiskSend = diskSent



if __name__ == "__main__":

    args = get_args()
    trainName = args.trainName
    main(trainName)

