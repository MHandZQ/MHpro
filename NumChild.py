# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NumChild.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NumChild(object):
    def setupUi(self, NumChild):
        NumChild.setObjectName("NumChild")
        NumChild.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/GoogleDownload/dna (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NumChild.setWindowIcon(icon)
        NumChild.setWindowOpacity(0.7)
        self.centralwidget = QtWidgets.QWidget(NumChild)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame1 = QtWidgets.QLabel(self.centralwidget)
        self.Frame1.setGeometry(QtCore.QRect(20, 10, 371, 211))
        self.Frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Frame1.setText("")
        self.Frame1.setObjectName("Frame1")
        self.TotalFrame1 = QtWidgets.QLabel(self.centralwidget)
        self.TotalFrame1.setGeometry(QtCore.QRect(470, 50, 71, 31))
        self.TotalFrame1.setFrameShape(QtWidgets.QFrame.Panel)
        self.TotalFrame1.setText("")
        self.TotalFrame1.setObjectName("TotalFrame1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 50, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 50, 51, 31))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 120, 241, 31))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 190, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 190, 51, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(470, 190, 71, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 320, 91, 31))
        self.label_6.setObjectName("label_6")
        self.TotalNumber = QtWidgets.QLabel(self.centralwidget)
        self.TotalNumber.setGeometry(QtCore.QRect(530, 320, 71, 31))
        self.TotalNumber.setFrameShape(QtWidgets.QFrame.Panel)
        self.TotalNumber.setText("")
        self.TotalNumber.setObjectName("TotalNumber")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.Frame1_2 = QtWidgets.QLabel(self.centralwidget)
        self.Frame1_2.setGeometry(QtCore.QRect(20, 210, 371, 211))
        self.Frame1_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Frame1_2.setText("")
        self.Frame1_2.setObjectName("Frame1_2")
        NumChild.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NumChild)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        NumChild.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NumChild)
        self.statusbar.setObjectName("statusbar")
        NumChild.setStatusBar(self.statusbar)

        self.retranslateUi(NumChild)
        QtCore.QMetaObject.connectSlotsByName(NumChild)

    def retranslateUi(self, NumChild):
        _translate = QtCore.QCoreApplication.translate
        NumChild.setWindowTitle(_translate("NumChild", "Sperm Count"))
        self.label_2.setText(_translate("NumChild", "Total"))
        self.label_3.setText(_translate("NumChild", "Frames"))
        self.label.setText(_translate("NumChild", "Sperm Count of Specific Frames"))
        self.label_4.setText(_translate("NumChild", "Input"))
        self.label_5.setText(_translate("NumChild", "Frames"))
        self.label_6.setText(_translate("NumChild", "Sperm Count"))
        self.pushButton.setText(_translate("NumChild", "OK"))
