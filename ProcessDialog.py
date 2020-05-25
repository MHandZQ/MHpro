# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProcessDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(392, 155)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/GoogleDownload/240_F_321593124_8wldrdGkdQuAa8w8GxvhOli1jGzPoWwn.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(0.7)
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 221, 51))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(200, 40, 91, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(198, 200, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 200, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 200, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton.setPalette(palette)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setText("")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Processing"))
        self.label.setText(_translate("Dialog", "Wait a Minute, Processing..."))
