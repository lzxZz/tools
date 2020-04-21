#!/usr/bin/env python3
import sys
from os import system
import time



def Clock_Delay(t):

    print("现在时间:" + time.strftime('%H:%M:%S',time.localtime(time.time())))
    print (t)
    if t[-1] == 'm' or t[-1] == 'M':
        t = int(t[0:-1]) * 60
    else :
        t = int(t)
    print("完成时间:" + time.strftime('%H:%M:%S',time.localtime(time.time() + t)))
    system("sleep " + str(t))
    

def VoiceNotify():
    system("mplayer /opt/clock/clock.mp3")

def Main():
    if len(sys.argv) != 2 :
        print("请输入一个参数!")
        exit(0)
    t = sys.argv[1]
    Clock_Delay(t)
    VoiceNotify()


if __name__ == "__main__":
    Main()