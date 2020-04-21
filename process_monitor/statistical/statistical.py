#!/usr/bin/env python3

import sys
import operator
from prettytable import PrettyTable

def Print(result):
    times = 0
    # sorted(result.values(), reverse=True)
    result_list  = []
    for (k,v) in result.items():
        times += v
        # print(k, v, "\n")
        result_list.append((k,v))
    

    result_list =  sorted(result_list, key=operator.itemgetter(1), reverse=True)
    table = PrettyTable(["耗时百分比", "运行小时数","运行分钟数", "运行秒数", "进程名称"])
    table.align["进程名称"] = "l"
    table.padding_width = 2
    totolHours = times/60/60  #运行小时数
    print("运行时间\t" , times/60 , "分钟")
    # table.add_row(["123"])
    for k,v in result_list:
        # print(int(v/60) , "分钟\t",  k)
        table.add_row(["%.f%%" % (v/times*100),  "%.2f小时" % (v/60/60),"%.f分钟" % (v/60), "%.f秒" %(v), k])

    print(table)

    


def Main(argc, argv):
    if (argc != 2):
        print("参数错误, 用法: statistical.py 2019-07-01.log")
    result = dict()
    f = open(argv[1])
    # print(len(f.readlines()))
    lines = f.readlines()
    for line in lines:
        name = line[0:-1].split("\t\t")[1]
        # print(name)
        result[name] = result.get(name, 0) + 1

    Print(result)

if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv

    Main(argc, argv)