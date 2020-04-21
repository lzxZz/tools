#!/usr/bin/env python3

import os
import sys


argc = len(sys.argv)
argv = sys.argv


def Convert(file, recuse = True):
    print(file)
    if os.path.isfile(file):
            print("---", file)
            # Convert(file)
            f = open(file)
            lines = f.readlines()
            f.close();

            for line in lines:
                line = line.replace("\r\n", '\n')
                line = line.replace("\r", '')
            
            f = open(file+'.bak', 'w')
            f.writelines(lines)

    elif os.path.isdir(file):
        for file in os.listdir(file):

            Convert(file)



def Main(argc, argv):
    if (argc == 2):
        file = argv[1];
        Convert(file)
        
    #     else:
    #         print("错误")
    # elif (argc == 3):
    else:
        print("参数错误")
    



if __name__ == "__main__":
    Main(argc, argv)