from detector import *
import math

global acts
acts = []

def cal_distance(Reframe,GTframe):
    x1 = Reframe[0]
    y1 = Reframe[1]

    x2 = GTframe[0]
    y2 = GTframe[1]

    fx = x2-x1
    fy = y2-y1

    distance = np.sqrt(fx * fx + fy * fy)
    return distance

def cal_dir(rec1,rec2):
    dir = rec2[1]-rec1[1]
    return dir

def cal_speed(rec1,rec2):
    x = rec2[0]-rec1[0]
    y = rec2[1]-rec1[1]
    speed = math.sqrt(x*x+y*y)
    return  speed

def mtt(spt):
    speedth = spt
    Framelen = len(bbox)
    firstframe = bbox[0]
    i = 1
    while True:
        a = len(firstframe)
        if i > Framelen-1:
            break
        frame = bbox[i]
        n = 0
        b = len(frame)
        for j in range(0,a):
            for k in range(0,b):
                dis = cal_distance(firstframe[j],frame[k])
                if dis<50:
                    direction = cal_dir(firstframe[j],frame[k])
                    speed = cal_speed(firstframe[j],frame[k])
                    if direction>0 and speed>speedth:
                        n = n+1
        acts.append(n)
        n=0
        firstframe = bbox[i]
        i = i+1