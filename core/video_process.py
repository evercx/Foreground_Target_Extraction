# -*- coding: utf-8 -*-

import numpy as np
import cv2
import libbgs
import sys

class App:

    def __init__(self,videoSrc,bgs):
        self.bgs = bgs
        self.videoSrc = videoSrc
        print("视频地址:",videoSrc)

    def run(self):
        capture = cv2.VideoCapture(self.videoSrc)
        while not capture.isOpened():
            capture = cv2.VideoCapture(self.videoSrc)
            cv2.waitKey(1000)
            print("Wait for the header")

        while True:
            flag, frame = capture.read()
            if flag:
                img_output = self.bgs.apply(frame)
                img_bgmodel = self.bgs.getBackgroundModel();

                cv2.imshow('img_raw', frame)
                cv2.imshow('img_output', img_output)
                cv2.imshow('img_bgmodel', img_bgmodel)

                cv2.moveWindow('img_raw', 100, 100)
                cv2.moveWindow('img_output', 100, 300)
                cv2.moveWindow('img_bgmodel', 100, 500)
            else:
                cv2.waitKey(2000)
                break
            if 0xFF & cv2.waitKey(10) == 27:
                break

        cv2.waitKey(5000)
        cv2.destroyAllWindows()



