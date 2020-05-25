# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WornDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Worning(object):
    def setupUi(self, Worning):
        Worning.setObjectName("Worning")
        Worning.setWindowModality(QtCore.Qt.NonModal)
        Worning.resize(394, 166)
        self.centralwidget = QtWidgets.QWidget(Worning)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Cera PROModern Medium")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        Worning.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Worning)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 26))
        self.menubar.setObjectName("menubar")
        Worning.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Worning)
        self.statusbar.setObjectName("statusbar")
        Worning.setStatusBar(self.statusbar)

        self.retranslateUi(Worning)
        QtCore.QMetaObject.connectSlotsByName(Worning)

    def retranslateUi(self, Worning):
        _translate = QtCore.QCoreApplication.translate
        Worning.setWindowTitle(_translate("Worning", "Worning"))
        self.label.setText(_translate("Worning", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Please Select Sperm GIF Firstly!</span></p></body></html>"))
