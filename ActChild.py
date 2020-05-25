# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActChild.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ActChild(object):
    def setupUi(self, ActChild):
        ActChild.setObjectName("ActChild")
        ActChild.resize(716, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/GoogleDownload/dna (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ActChild.setWindowIcon(icon)
        ActChild.setWindowOpacity(0.7)
        self.centralwidget = QtWidgets.QWidget(ActChild)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame2 = QtWidgets.QLabel(self.centralwidget)
        self.Frame2.setGeometry(QtCore.QRect(20, 10, 411, 361))
        self.Frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Frame2.setText("")
        self.Frame2.setObjectName("Frame2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 190, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 300, 191, 31))
        self.label_2.setObjectName("label_2")
        self.ActNumber = QtWidgets.QLabel(self.centralwidget)
        self.ActNumber.setGeometry(QtCore.QRect(440, 340, 91, 31))
        self.ActNumber.setFrameShape(QtWidgets.QFrame.Panel)
        self.ActNumber.setText("")
        self.ActNumber.setObjectName("ActNumber")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 50, 41, 31))
        self.label_4.setObjectName("label_4")
        self.TotalFrame2 = QtWidgets.QLabel(self.centralwidget)
        self.TotalFrame2.setGeometry(QtCore.QRect(490, 50, 71, 31))
        self.TotalFrame2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.TotalFrame2.setFrameShape(QtWidgets.QFrame.Panel)
        self.TotalFrame2.setText("")
        self.TotalFrame2.setObjectName("TotalFrame2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 50, 51, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 100, 261, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(490, 140, 71, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 140, 51, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 140, 41, 31))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 240, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(440, 240, 91, 31))
        self.spinBox.setMaximum(20)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        ActChild.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ActChild)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 26))
        self.menubar.setObjectName("menubar")
        ActChild.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ActChild)
        self.statusbar.setObjectName("statusbar")
        ActChild.setStatusBar(self.statusbar)

        self.retranslateUi(ActChild)
        QtCore.QMetaObject.connectSlotsByName(ActChild)

    def retranslateUi(self, ActChild):
        _translate = QtCore.QCoreApplication.translate
        ActChild.setWindowTitle(_translate("ActChild", "Sperm Activity Detection"))
        self.label.setText(_translate("ActChild", "Sperm\'s Velocity"))
        self.label_2.setText(_translate("ActChild", "Number of Active Sperms"))
        self.label_4.setText(_translate("ActChild", "Total"))
        self.label_5.setText(_translate("ActChild", "Frames"))
        self.label_6.setText(_translate("ActChild", "Active Sperms of Specific Frames"))
        self.label_7.setText(_translate("ActChild", "Frames"))
        self.label_8.setText(_translate("ActChild", "Input"))
        self.pushButton.setText(_translate("ActChild", "OK"))
