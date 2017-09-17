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


        frame_num = 0   #帧数

        json_list = []

        while True:
            # cv2.waitKey(500)
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

                print("white:",whitePoints," black:",blackPoints,"  Frame:",frame_num)
                d = {
                    0:frame_num,
                    1:whitePoints,
                    2:blackPoints
                }
                json_list.append(d)


                cv2.imshow('img_raw', frame)
                cv2.imshow('img_output', img_output)
                cv2.imshow('img_bgmodel', img_bgmodel)

                cv2.moveWindow('img_raw', 100, 100)
                cv2.moveWindow('img_output', 100, 300)
                cv2.moveWindow('img_bgmodel', 100, 500)
            else:
                cv2.waitKey(1500)
                cv2.destroyAllWindows()
                break
            if 0xFF & cv2.waitKey(10) == 27:
                cv2.destroyAllWindows()
                break
        print("帧数:",frame_num)

        with open('./video-json/overpass.json', 'w') as json_file:
            json_file.write(json.dumps(json_list))
            print("写入完毕")

        cv2.waitKey(1500)
        cv2.destroyAllWindows()



if __name__ == '__main__':

    App('../dataset/NoShake_StaticBg/airport.avi',"DPMean").run()
