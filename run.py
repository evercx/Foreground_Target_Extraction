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
    elif inputMessage == "3":
        print("你选择的是算法3:LBMixtureOfGaussians")
        return "LBMixtureOfGaussians"
    elif inputMessage == "q":
        sys.exit(0)
    else:
        print("你输入的字符无效")
        return None

def choose_video(inputMessage):

    video_dict = {
        "0":{
            "msg": "你选择的是视频0:不晃动的动态背景的水流",
            "src": "./dataset/NoShake_MoveBg/waterSurface.avi"
        },
        "1": {
            "msg": "你选择的是视频1:不晃动的静态背景的机场",
            "src": "./dataset/NoShake_StaticBg/airport.avi"
        },
        "2": {
            "msg": "你选择的是视频2:不晃动的静态背景的大厅",
            "src": "./dataset/NoShake_StaticBg/hall.avi"
        },
        "3": {
            "msg": "你选择的是视频3:不晃动的静态背景的办公室",
            "src": "./dataset/NoShake_StaticBg/office.avi"
        },
        "4": {
            "msg": "你选择的是视频4:不晃动的静态背景的行人",
            "src": "./dataset/NoShake_StaticBg/pedestrian.avi"
        },
        "5": {
            "msg": "你选择的是视频5:不晃动的静态背景的烟",
            "src": "./dataset/NoShake_StaticBg/smoke.avi"
        },
        "6": {
            "msg": "你选择的是视频6:晃动的车6",
            "src": "./dataset/Shake/cars6.avi"
        },
        "7": {
            "msg": "你选择的是视频7:晃动的车7",
            "src": "./dataset/Shake/cars7.avi"
        },
        "8": {
            "msg": "你选择的是视频8:晃动的人1",
            "src": "./dataset/Shake/people1.avi"
        },
        "9": {
            "msg": "你选择的是视频9:晃动的人2",
            "src": "./dataset/Shake/people2.avi"
        },
        "10": {
            "msg": "你选择的是视频10:校园",
            "src": "./dataset/Check_Foreground/Campus.avi"
        },
        "11": {
            "msg": "你选择的是视频11:窗帘",
            "src": "./dataset/Check_Foreground/Curtain.avi"
        },
        "12": {
            "msg": "你选择的是视频12:电动扶梯",
            "src": "./dataset/Check_Foreground/Escalator.avi"
        },
        "13": {
            "msg": "你选择的是视频13:喷泉",
            "src": "./dataset/Check_Foreground/Fountain.avi"
        },
        "14": {
            "msg": "你选择的是视频14:大厅",
            "src": "./dataset/Check_Foreground/hall.avi"
        },
        "15": {
            "msg": "你选择的是视频15:休息室",
            "src": "./dataset/Check_Foreground/Lobby.avi"
        },
        "16": {
            "msg": "你选择的是视频16:办公室",
            "src": "./dataset/Check_Foreground/office.avi"
        },
        "17": {
            "msg": "你选择的是视频17:天桥",
            "src": "./dataset/Check_Foreground/overpass.avi"
        },
    }



    if inputMessage == "q":
        sys.exit(0)
    elif video_dict.has_key(inputMessage):
        print(video_dict[inputMessage]["msg"])
        return video_dict[inputMessage]["src"]
    else:
        print("你输入的字符无效")
        return None



def main():


    while True:

        print("\n\t\t\t\t\t\t前景目标提取程序")
        print("\n============================================================================")
        print("0:DPMean\t\t 1:LBP_MRF\t\t 2:MultiLayer \t\t 3:LBMixtureOfGaussians \t\tq:退出本程序")
        print("============================================================================")
        inputMessage = raw_input("请选择算法: ");
        algorithms = choose_algorithms(inputMessage)
        print("\n============================================================================")
        print("0:不晃动的动态背景的水流\t\t\t\t\t1:不晃动的静态背景的机场")
        print("2:不晃动的静态背景的大厅\t\t\t\t\t3:不晃动的静态背景的办公室")
        print("4:不晃动的静态背景的行人\t\t\t\t\t5:不晃动的静态背景的烟")
        print("6:晃动的车6\t\t\t\t\t\t\t\t7:晃动的车7")
        print("8:晃动的人1\t\t\t\t\t\t\t\t9:晃动的人2")
        print("10:检测视频:校园\t\t\t\t\t\t\t11:检测视频:窗帘")
        print("12:检测视频:电动扶梯\t\t\t\t\t\t13:检测视频:喷泉")
        print("14:检测视频:大厅\t\t\t\t\t\t\t15:检测视频:休息室")
        print("16:检测视频:办公室\t\t\t\t\t\t17:检测视频:天桥")
        print("q:退出本程序")
        print("============================================================================")
        inputMessage = raw_input("请选择视频: ");
        videoSrc = choose_video(inputMessage)

        if videoSrc != None and algorithms != None:
            print("播放视频...")
            video.App(videoSrc,algorithms).run()
            print("视频播放完毕...")

if __name__ == '__main__':
    main()


