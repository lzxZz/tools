#!/usr/bin/env python3

import os
import time


CMDGetActiveWindowsPID = "xdotool getactivewindow getwindowpid"
env_dist = os.environ



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
    id = GetCmdOutPut("xdotool getactivewindow")
    title = GetCmdOutPut("xdotool getwindowname " + id)
    pid = GetActiveWindowsPID()
    process_name = GetProgramNameByID(pid)
    
    
    
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # print(now, GetProgramNameByID(id))
    
    out_string = (now +"\t---\t"+ process_name+ "\t---\t" + title + "\n")
    
    # print(out_string)

    
    log_dir = env_dist.get("LZX_MONITOR_LOG_DIR")
    # print(log_dir)
    if log_dir == None :
        log_dir = GetCmdOutPut("cd ~ && pwd")
        
    if not os.path.exists(log_dir):
        os.system("mkdir -p " + log_dir)

    f = open(log_dir + "/" + now.split(" ")[0] +".log", 'a')

    f.write(out_string)
    f.close()


    print("进程监控中")


if __name__ == "__main__":
    Main()