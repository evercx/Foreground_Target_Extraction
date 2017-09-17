# -*- coding: utf-8 -*-

import numpy as np
import cv2
import libbgs
import sys

import core.video_process as video




# bgs = libbgs.DPMean()?
# bgs = libbgs.LBP_MRF()?
# bgs = libbgs.MultiLayer()?


def choose_algorithms(inputMessage):

    if inputMessage == "0":
        print("你选择的是算法0:DPMean")
        return "DPMean"
    elif inputMessage == "1":
        print("你选择的是算法1:LBP_MRF")
        return "LBP_MRF"
    elif inputMessage == "2":
        print("你选择的是算法2:MultiLayer")
        return "MultiLayer"
    elif inputMessage == "q":
        sys.exit(0)
    else:
        print("你输入的字符无效")
        return None

def choose_video(inputMessage):

    if inputMessage == "0":
        print("你选择的是视频0:不晃动的动态背景的水流")
        return "./dataset/NoShake_MoveBg/waterSurface.avi"
    elif inputMessage == "1":
        print("你选择的是视频1:不晃动的静态背景的机场")
        return "./dataset/NoShake_StaticBg/airport.avi"
    elif inputMessage == "2":
        print("你选择的是视频2:不晃动的静态背景的大厅")
        return "./dataset/NoShake_StaticBg/hall.avi"
    elif inputMessage == "3":
        print("你选择的是视频3:不晃动的静态背景的办公室")
        return "./dataset/NoShake_StaticBg/office.avi"
    elif inputMessage == "4":
        print("你选择的是视频4:不晃动的静态背景的行人")
        return "./dataset/NoShake_StaticBg/pedestrian.avi"
    elif inputMessage == "5":
        print("你选择的是视频5:不晃动的静态背景的烟")
        return "./dataset/NoShake_StaticBg/smoke.avi"
    elif inputMessage == "6":
        print("你选择的是视频6:晃动的车6")
        return "./dataset/Shake/cars6.avi"
    elif inputMessage == "7":
        print("你选择的是视频7:晃动的车7")
        return "./dataset/Shake/cars7.avi"
    elif inputMessage == "8":
        print("你选择的是视频8:晃动的人1")
        return "./dataset/Shake/people1.avi"
    elif inputMessage == "9":
        print("你选择的是视频9:晃动的人2")
        return "./dataset/Shake/people2.avi"
    elif inputMessage == "q":
        sys.exit(0)
    else:
        print("你输入的字符无效")
        return None

def main():


    while True:
        print("前景目标提取程序\n")
        print("0:DPMean\t\t 1:LBP_MRF\t\t 2:MultiLayer \t\tq:退出本程序")
        inputMessage = raw_input("请选择算法: ");
        algorithms = choose_algorithms(inputMessage)
        print("\n0:不晃动的动态背景的水流")
        print("1:不晃动的静态背景的机场")
        print("2:不晃动的静态背景的大厅")
        print("3:不晃动的静态背景的办公室")
        print("4:不晃动的静态背景的行人")
        print("5:不晃动的静态背景的烟")
        print("6:晃动的车6")
        print("7:晃动的车7")
        print("8:晃动的人1")
        print("9:晃动的人2")
        print("q:退出本程序")
        inputMessage = raw_input("请选择视频: ");
        videoSrc = choose_video(inputMessage)

        if videoSrc != None and algorithms != None:
            print("播放视频...")
            video.App(videoSrc,algorithms).run()
            print("视频播放完毕...")

if __name__ == '__main__':
    main()


