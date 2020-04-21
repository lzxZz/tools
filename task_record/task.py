#!/usr/bin/env python3


import sys
from os import system
import clock
argv =  sys.argv
argc = len(argv)



def Main(argc, argv):
    if argc != 3:
        print("用法： Task time task_name")
        exit(-1)
    
    t = argv[1]
    name = argv[2]
    

    print(t)
    print(name)
    system("echo " +  name +" > /home/lzx/.todo")
    # system("clock.py " + t )
    clock.Clock_Delay(t)
    system("notify-send 任务'>>'" + name  + "'<<'完成")
    system("echo '无任务' > /home/lzx/.todo")
    clock.VoiceNotify()

if __name__ == "__main__":
    Main(argc, argv)