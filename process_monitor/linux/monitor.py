#!/usr/bin/env python3

import os
import time

log_dir = "/tmp/" #设置日志根目录

CMDGetActiveWindowsPID = "xdotool getactivewindow getwindowpid"

def GetCmdOutPut(cmd):
    return os.popen(cmd).read()


def GetActiveWindowsPID():
    return GetCmdOutPut(CMDGetActiveWindowsPID)

def GetProgramNameByID(id):
    cmd = "ps " + id
    result = GetCmdOutPut(cmd)
    ll = result.split("\n")[1]
    # print(type(result))

    ll = ll.split(' ')

    while ('' in ll):
        ll.remove('')

    # print(ll)

    return ll[4]

def Main():
    # print (GetCmdOutPut("echo monitor"))
    
    id = GetActiveWindowsPID()
    
    
    
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # print(now, GetProgramNameByID(id))
    
    f = open(log_dir + now.split(" ")[0] +".log", 'a')
    f.write(now +"\t\t"+ GetProgramNameByID(id)+"\n")
    print("进程监控中")


if __name__ == "__main__":
    Main()