import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWin import *
from NumChild import *
from ActChild import *
from ProcessDialog import *
from WornDialog import *
from mot import *
from detector import *
from ProcessImg import *


class WorkThread(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread,self).__init__()

    def run(self):
        G2I(main.fileName)
        dec(main.fileName)
        self.trigger.emit()         #循环完毕后发出信号

class Dialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.label.setText("正在处理中，请稍等")
        self.show()

class Worn(QMainWindow,Ui_Worning):
    def __init__(self):
        super(Worn, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.label.setText("请先选择需要处理的精子gif")
        self.show()

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

    def openfile(self):
        self.fileName, self.fileType = QFileDialog.getOpenFileName(self.Read, "选择gif", "E:\\", "*.gif;;All Files(*)")
        gif = QtGui.QMovie(self.fileName)
        self.Display.setScaledContents(True)
        self.Display.setMovie(gif)
        gif.start()



class NumChild(QMainWindow,Ui_NumChild):
    def __init__(self):
        super(NumChild, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.show()

    def totalframe1(self):
        temp = len(nums)
        self.TotalFrame1.setText(str(temp))

    def readfile(self):
        self.frame = self.lineEdit1.text()
        imgName1 = "./sperm/%s.jpg" % str(self.frame)  # 存储图片的路径
        imgName1_2 = "./processimg/%s.jpg"%str(self.frame)
        jpg1 = QtGui.QPixmap(imgName1)
        self.Frame1.setPixmap(jpg1)
        self.Frame1.setScaledContents(True)
        jpg2 = QtGui.QPixmap(imgName1_2)
        self.Frame1_2.setPixmap(jpg2)
        self.Frame1_2.setScaledContents(True)
        b = int(self.frame)
        temp = nums[b-1]
        self.TotalNumber.setText(str(temp))



class ActChild(QMainWindow,Ui_ActChild):
    def __init__(self):
        super(ActChild, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.show()

    def totalframe2(self):
        temp = len(nums)-2
        if temp > 0:
            self.TotalFrame2.setText(str(temp))
        else:
            self.TotalFrame2.setText(str(0))

    def readact(self):
        speed = self.spinBox.value()
        speed = int(speed)
        mtt(speed)
        self.frame2 = self.lineEdit2.text()
        imgName2 = "./LFlowDec/%s.jpg" % str(self.frame2)
        jpg2 = QtGui.QPixmap(imgName2)
        self.Frame2.setPixmap(jpg2)
        self.Frame2.setScaledContents(True)
        c = int(self.frame2)
        temp = acts[c-1]
        self.ActNumber.setText(str(temp))
        del acts[:]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    workThread = WorkThread()
    main = Main()
    nch = NumChild()
    ach = ActChild()
    pdg = Dialog()
    won = Worn()
    main.show()

    main.Read.clicked.connect(main.openfile)
    main.Number.clicked.connect(nch.OPEN)
    main.Number.clicked.connect(nch.totalframe1)
    main.Activity.clicked.connect(ach.OPEN)
    main.Activity.clicked.connect(ach.totalframe2)

    main.Process.clicked.connect(pdg.OPEN)
    main.Process.clicked.connect(workThread.run)
    workThread.trigger.connect(pdg.close)
    workThread.exit()

    nch.pushButton.clicked.connect(nch.readfile)
    ach.pushButton.clicked.connect(ach.readact)
    sys.exit(app.exec_())