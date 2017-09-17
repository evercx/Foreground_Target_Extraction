# -*- coding: utf-8 -*-

import numpy as np
import cv2
import libbgs
import sys

class App:

    def __init__(self,videoSrc,bgsName):

        self.videoSrc = videoSrc
        self.bgsName = bgsName
        #print("视频地址:",videoSrc)

    def run(self):
        capture = cv2.VideoCapture(self.videoSrc)
        pic = capture.read()
        print(type(pic))
        print(pic)
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

        while True:
            flag, frame = capture.read()
            #print(frame)
            img_output = None
            img_bgmodel = None
            if flag:
                img_output = bgs.apply(frame)
                img_bgmodel = bgs.getBackgroundModel();

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

        cv2.waitKey(1500)
        cv2.destroyAllWindows()



if __name__ == '__main__':

    App('../dataset/NoShake_StaticBg/airport.avi',"DPMean").run()
