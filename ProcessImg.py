from skimage import measure
from detector import *

nums = []
global framecount
framecount = 1

##输入：一张二值图像
##输出：会返回去除小面积的二值图像

def save_want_objects(img):
    labels = measure.label(img)  # 返回打上标签的img数组
    jj = measure.regionprops(labels)  # 找出连通域的各种属性。  注意，这里jj找出的连通域不包括背景连通域
    if len(jj) == 1:
        out = img
    else:
        # 通过与质心之间的距离进行判断
        num = labels.max()  #连通域的个数
        del_array = np.array([0] * (num + 1))  # 生成一个与连通域个数相同的空数组来记录需要删除的区域（从0开始，所以个数要加1）
        for k in range(num):  # 这里如果遇到全黑的图像的话会报错
            th_area = 100# 阈值面积
            k_area = jj[k].area# 将元组转换成array
            if k_area > th_area:
                save_index = k + 1
                del_array[save_index] = 1#大于面积阈值的连通域置1
                del_mask = del_array[labels]#掩膜
        out = img * del_mask #0*1=0，1*1=1
    return out

def processImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 把输入图像灰度化
    blur_image = cv2.GaussianBlur(gray_image, (3, 3), 0)  # 高斯滤波
    ret2, binary_image = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 高斯滤波后用OTSU二值化
    # print("%s"%ret2)
    size = 3
    kernel = np.ones((size, size), dtype=np.uint8)
    img_close = cv2.erode(cv2.dilate(binary_image, kernel), kernel)  # 二值图像闭运算
    image = 255 - img_close  # 二值图像取反
    # 将提取的视频帧存储进imgPath
    out_img = save_want_objects(image)
    return out_img

def G2I(path):
    # 利用VideoCapture捕获视频，也可用于gif读取
    cap = cv2.VideoCapture(path)  # 要分解的视频的路径
    #判断是否打开gif
    if cap.isOpened():
        flag = 1
    else:
        flag = 0

    if flag == 1:
        global framecount
        while True:
            ret, frame = cap.read()  # 读取gif帧
            if ret == False:  # 判断是否读取成功
                break
            #print('统计精子数目及检测精子活性，正在拆解第{}帧...'.format(i))
            imgPath = "./sperm/%s.jpg" % str(framecount)  # 存储图片的路径
            cv2.imwrite(imgPath, frame)  # 将提取的视频帧存储进imgPath
            out_img = processImage(frame)
            labels = measure.label(out_img)  # 返回打上标签的img数组
            tt = measure.regionprops(labels)  # 找出连通域的各种属性
            num = labels.max()
            nums.append(num)
            #print("第{}帧含有精子数目：".format(i), num)
            #for j in range(num):
                #print("面积：", tt[j].area)
            imgPath = "./processimg/%s.jpg" % str(framecount)  # 存储图片的路径
            cv2.imwrite(imgPath, out_img)  # 将提取的视频帧存储进imgPath
            framecount += 1