import argparse
import cv2
import numpy as np

array = []
bbox = []

def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1)
    fx, fy = flow[y.astype(int), x.astype(int)].T
    lines = np.vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    cv2.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (x2, y2) in lines:
        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    return vis


def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:, :, 0], flow[:, :, 1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx * fx + fy * fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[..., 0] = ang * (180 / np.pi / 2)
    hsv[..., 1] = 255
    hsv[..., 2] = np.minimum(v * 4, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr

def dec(path):
    cam = cv2.VideoCapture(path)
    ret, prev = cam.read()

    prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    i = 1
    bounding = []

    while True:
        ret, img = cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w, _ = img.shape
        flow = np.zeros((h, w, 1), np.float32)
        flow = cv2.calcOpticalFlowFarneback(prevgray, gray, flow, 0.5, 5, 15, 3, 5, 1, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        prevgray = gray

        imgPath = "./LFlow/%s.jpg" % str(i)  # 存储图片的路径
        cv2.imwrite(imgPath, draw_flow(gray, flow))  # 将提取的视频帧存储进imgPath
        cv2.imshow('flow', draw_flow(gray, flow))
        gray1 = cv2.cvtColor(draw_hsv(flow), cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray1, 10, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # loop over the contours
        for c in cnts:
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 200:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            bounding.append((x+w/2, y+h/2))#目标矩形框中心
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)#(x,y)为左上点坐标，(x+w,y+h)为右下点坐标
            text = "Sperm's Activity"
        cv2.putText(img, "Dectector: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        bbox.append(bounding)
        bounding = []
        imgPath = "./LFlowDec/%s.jpg" % str(i)  # 存储图片的路径
        cv2.imwrite(imgPath, img)  # 将提取的视频帧存储进imgPath
        i = i+1
        #cv2.imshow('Image', img)
        ch = cv2.waitKey(60) & 0xff
        if ch == 27:
          break
    cv2.destroyAllWindows()