# -*- coding: utf-8 -*-

import numpy as np
import cv2
import libbgs


#光流检测的参数
lk_params = dict( winSize  = (15, 15),#搜索窗口的大小
                  maxLevel = 2,#最大的金字塔层数
                  # 指定停止条件，具体没懂
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

#角点检测的参数
feature_params = dict( maxCorners = 500,#最大角点数
                       qualityLevel = 0.3,#角点最低质量
                       minDistance = 7,#角点间最小欧式距离
                       blockSize = 7 )#这个没懂，我做角点检测时只设置了上面几个参数，望指教


class App:
    def __init__(self, video_src):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = cv2.VideoCapture(video_src)
        self.frame_idx = 0

    def run(self):

        while True:
            cv2.waitKey(500)
            ret, frame = self.cam.read()#通过摄像头获取一张图片
            if ret:
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转化为灰度图
                vis = frame.copy()#赋值frame的值，不覆盖frame本身

            if len(self.tracks) > 0:#检测到角点后进行光流跟踪
                img0, img1 = self.prev_gray, frame_gray
                p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)#对np数组进行重塑
                #前一帧的角点和当前帧的图像作为输入来得到角点在当前帧的位置，有点绕，具体实现有兴趣就去看源码吧
                p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
                #当前帧跟踪到的角点及图像和前一帧的图像作为输入来找到前一帧的角点位置
                p0r, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
                d = abs(p0-p0r).reshape(-1, 2).max(-1)#得到角点回溯与前一帧实际角点的位置变化关系
                good = d < 1#判断d内的值是否小于1，大于1跟踪被认为是错误的跟踪点，为什么是1不知道
                new_tracks = []
                #将跟踪正确的点列入成功跟踪点
                for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                    if not good_flag:
                        continue
                    tr.append((x, y))
                    if len(tr) > self.track_len:
                        del tr[0]
                    new_tracks.append(tr)
                    cv2.circle(vis, (x, y), 2, (0, 255, 0), -1)#画圆
                self.tracks = new_tracks

                #以上一振角点为初始点，当前帧跟踪到的点为终点划线
                cv2.polylines(vis, [np.int32(tr) for tr in self.tracks], False, (0, 255, 0))

                #draw_str(vis, (20, 20), 'track count: %d' % len(self.tracks))

            if self.frame_idx % self.detect_interval == 0:#每5帧检测一次特征点
                mask = np.zeros_like(frame_gray)#初始化和视频大小相同的图像
                mask[:] = 255#将mask赋值255也就是算全部图像的角点
                for x, y in [np.int32(tr[-1]) for tr in self.tracks]:#跟踪的角点画圆
                    cv2.circle(mask, (x, y), 5, 0, -1)
                p = cv2.goodFeaturesToTrack(frame_gray, mask = mask, **feature_params)#角点检测
                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        self.tracks.append([(x, y)])#将检测到的角点放在待跟踪序列中


            self.frame_idx += 1
            self.prev_gray = frame_gray

            #bgs = libbgs.DPMean()
            #img_output = bgs.apply(frame)
            cv2.imshow('lk_track', vis)
            #cv2.imshow('res',img_output)

            cv2.moveWindow('lk_track', 100, 100)
            #cv2.moveWindow('res', 100, 300)

            ch = 0xFF & cv2.waitKey(1)#按esc退出
            if ch == 27:
                break

def main():
    # import sys
    # try: video_src = sys.argv[1]
    # except: video_src = 0
    #
    # print __doc__
    # App(video_src).run()


    video_src = "dataset/people_doudong.avi"
    App(video_src).run()





    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
