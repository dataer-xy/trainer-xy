
import subprocess
import time
import os

from trainer.core import sysinfo



def test_cmd():
    trainName = "20191118152056"
    pyFile = os.path.abspath(sysinfo.__file__)
    cmd = "python {pyFile} \"{trainName}\"".format(pyFile=pyFile,trainName=trainName)
    sysInfoSubprocess = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    # sysInfoSubprocess = subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

    # print(sysInfoSubprocess.pid)

    # time.sleep(120)
    # sysInfoSubprocess.poll()

    # sysInfoSubprocess.kill() # 在 Windows 上， kill() 是 terminate() 的别名。

    print("end")


def test_cmd_1():
    trainName = "20191118152056"
    cmd = "python sysinfo.py {trainName}".format(trainName=trainName)
    sysInfoSubprocess = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

    print(sysInfoSubprocess.pid)

    sysInfoSubprocess.poll()

    sysInfoSubprocess.kill() # 在 Windows 上， kill() 是 terminate() 的别名。
 


def __main():
    test_cmd()
    # test_cmd_1()

if __name__ == "__main__":
    __main()

