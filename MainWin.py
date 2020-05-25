# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 509)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/GoogleDownload/dna (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.7)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Display = QtWidgets.QLabel(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(10, 20, 481, 421))
        self.Display.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Display.setAcceptDrops(False)
        self.Display.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Display.setLineWidth(5)
        self.Display.setMidLineWidth(0)
        self.Display.setText("")
        self.Display.setTextFormat(QtCore.Qt.AutoText)
        self.Display.setScaledContents(False)
        self.Display.setObjectName("Display")
        self.Process = QtWidgets.QPushButton(self.centralwidget)
        self.Process.setGeometry(QtCore.QRect(510, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cera PROModern Medium")
        self.Process.setFont(font)
        self.Process.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Process.setAutoDefault(True)
        self.Process.setObjectName("Process")
        self.Number = QtWidgets.QPushButton(self.centralwidget)
        self.Number.setGeometry(QtCore.QRect(510, 250, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cera PROModern Medium")
        self.Number.setFont(font)
        self.Number.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Number.setAutoDefault(True)
        self.Number.setObjectName("Number")
        self.Activity = QtWidgets.QPushButton(self.centralwidget)
        self.Activity.setGeometry(QtCore.QRect(510, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cera PROModern Medium")
        self.Activity.setFont(font)
        self.Activity.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Activity.setAutoRepeat(False)
        self.Activity.setAutoDefault(True)
        self.Activity.setObjectName("Activity")
        self.Read = QtWidgets.QPushButton(self.centralwidget)
        self.Read.setGeometry(QtCore.QRect(510, 70, 101, 41))
        self.Read.setAutoFillBackground(True)
        self.Read.setStyleSheet("font: 57 9pt \"Cera PROModern Medium\";")
        self.Read.setAutoDefault(True)
        self.Read.setDefault(False)
        self.Read.setFlat(False)
        self.Read.setObjectName("Read")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sperm Count and Activity Detection"))
        self.Process.setText(_translate("MainWindow", "Process"))
        self.Number.setText(_translate("MainWindow", "Count"))
        self.Activity.setText(_translate("MainWindow", "Detect"))
        self.Read.setText(_translate("MainWindow", "Select"))
