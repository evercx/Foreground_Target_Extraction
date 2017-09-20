# -*- coding: utf-8 -*-

import numpy as np
import cv2
import libbgs
import sys
import json

class App:

    def __init__(self,videoSrc,bgsName):

        self.videoSrc = videoSrc
        self.bgsName = bgsName
        self.threshold = 5
        #print("视频地址:",videoSrc)

    def run(self):
        capture = cv2.VideoCapture(self.videoSrc)

        # pic = capture.read()
        # pic = pic[1]
        # pic_np = np.array(pic)
        # print pic_np.shape
        # print len(pic_np[0])
        # pic = cv2.resize(pic, (160, 200))
        # cv2.imshow('d', pic)

        while not capture.isOpened():
            capture = cv2.VideoCapture(self.videoSrc)
            cv2.waitKey(1000)
            print("Wait for the header")

        if self.bgsName == "DPMean":
            bgs = libbgs.DPMean()
        elif self.bgsName == "LBP_MRF":
            bgs = libbgs.LBP_MRF()
        elif self.bgsName == "MultiLayer":
            bgs = libbgs.MultiLayer()
        elif self.bgsName == "LBMixtureOfGaussians":
            bgs = libbgs.LBMixtureOfGaussians()

        fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()



        frame_num = 0   #帧数

        json_list = []
        ForegroundTargetList = []

        begin_frame = -1
        end_frame = -1
        beginP = -1

        while True:
            cv2.waitKey(1000)
            frame_num += 1
            flag, frame = capture.read()

            #print(frame)
            img_output = None
            img_bgmodel = None
            if flag:
                img_output = bgs.apply(frame)
                img_bgmodel = bgs.getBackgroundModel()

                # print(img_output.shape)

                whitePoints = 0
                blackPoints = 0
                for i in range(0,len(img_output)):
                    for j in range(0,len(img_output[i])):
                        if img_output[i][j] == 255:
                            whitePoints += 1
                        else:
                            blackPoints += 1

                d = {
                    0:frame_num,
                    1:whitePoints,
                    2:blackPoints,
                    3:whitePoints / float(whitePoints + blackPoints) * 100
                }
                json_list.append(d)
                print("white:", d[1], " black:", d[2], " Proportion:",d[3],"  Frame:", frame_num)

                if d[3] >= self.threshold and begin_frame == -1:
                    begin_frame = frame_num
                    beginP = d[3]
                if d[3] < self.threshold and begin_frame != -1:
                    end_frame = frame_num - 1
                    ForegroundTargetList.append({"begin":begin_frame,"end":end_frame,"beginP":beginP,"endP":d[3]})
                    begin_frame = -1
                    end_frame = -1
                cv2.imshow('img_raw', frame)
                cv2.imshow('img_output', img_output)
                #cv2.imshow('img_bgmodel', img_bgmodel)

                cv2.moveWindow('img_raw', 100, 100)
                cv2.moveWindow('img_output', 300, 100)
                #cv2.moveWindow('img_bgmodel', 100, 500)

                # opencv自带的高斯混合模型
                fgmask = fgbg.apply(frame)
                cv2.imshow('gaussians', fgmask)
                cv2.moveWindow('gaussians', 500, 100)

            else:
                cv2.waitKey(1500)
                cv2.destroyAllWindows()
                break
            if 0xFF & cv2.waitKey(10) == 27:
                cv2.destroyAllWindows()
                break
        print("帧数:",frame_num)
        for i in range(len(ForegroundTargetList)):
            print(ForegroundTargetList[i]["begin"],ForegroundTargetList[i]["end"])
        print("=============================")

        # with open('./video-json/overpass .json', 'w') as json_file:
        #     json_file.write(json.dumps(json_list))
        #     print("写入完毕")

        cv2.waitKey(1500)
        cv2.destroyAllWindows()



if __name__ == '__main__':

    App('../dataset/NoShake_StaticBg/airport.avi',"DPMean").run()
