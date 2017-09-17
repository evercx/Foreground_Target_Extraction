# -*- coding: utf-8 -*-

import numpy as np
import cv2
import libbgs
import sys



# bgs = libbgs.DPMean()?
# bgs = libbgs.LBP_MRF()?
# bgs = libbgs.MultiLayer()?


def choose_algorithms(inputMessage):

    # algorithms = []
    # algorithms.append(libbgs.DPMean())
    # algorithms.append(libbgs.LBP_MRF())
    # algorithms.append(libbgs.MultiLayer())


    if inputMessage == "0":
        print("你选择的是算法0:DPMean")
        return libbgs.DPMean()
    elif inputMessage == "1":
        print("你选择的是算法1:LBP_MRF")
        return libbgs.LBP_MRF()
    elif inputMessage == "2":
        print("你选择的是算法2:MultiLayer")
        return libbgs.MultiLayer()
    elif inputMessage == "q":
        sys.exit(0)
    else:
        print("你输入的字符无效")

def main():




    while True:
        print("前景目标提取程序\n")
        print("0:DPMean\t\t 1:LBP_MRF\t\t 2:MultiLayer \t\tq:退出本程序")
        inputMessage = raw_input("请选择算法: ");
        choose_algorithms(inputMessage)



if __name__ == '__main__':
    main()


