# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(984, 502)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Israel))
        self.flirIP = QtWidgets.QLineEdit(Dialog)
        self.flirIP.setGeometry(QtCore.QRect(754, 21, 133, 20))
        self.flirIP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.flirIP.setObjectName("flirIP")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(680, 20, 67, 21))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(680, 280, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.connect = QtWidgets.QPushButton(Dialog)
        self.connect.setGeometry(QtCore.QRect(890, 20, 81, 23))
        self.connect.setObjectName("connect")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(820, 120, 21, 21))
        self.label_22.setObjectName("label_22")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(680, 90, 291, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(680, 120, 31, 21))
        self.label_20.setObjectName("label_20")
        self.atmT = QtWidgets.QLineEdit(Dialog)
        self.atmT.setGeometry(QtCore.QRect(760, 120, 51, 21))
        self.atmT.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.atmT.setObjectName("atmT")
        self.setAtmT = QtWidgets.QPushButton(Dialog)
        self.setAtmT.setGeometry(QtCore.QRect(850, 120, 121, 21))
        self.setAtmT.setObjectName("setAtmT")
        self.shootNow = QtWidgets.QPushButton(Dialog)
        self.shootNow.setGeometry(QtCore.QRect(890, 50, 81, 21))
        self.shootNow.setObjectName("shootNow")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(780, 380, 16, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(680, 380, 51, 21))
        self.label_26.setObjectName("label_26")
        self.IntervalTime = QtWidgets.QLineEdit(Dialog)
        self.IntervalTime.setGeometry(QtCore.QRect(740, 380, 31, 21))
        self.IntervalTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IntervalTime.setObjectName("IntervalTime")
        self.IntervalSet = QtWidgets.QPushButton(Dialog)
        self.IntervalSet.setGeometry(QtCore.QRect(870, 380, 101, 21))
        self.IntervalSet.setObjectName("IntervalSet")
        self.LogStart = QtWidgets.QPushButton(Dialog)
        self.LogStart.setGeometry(QtCore.QRect(680, 410, 291, 21))
        self.LogStart.setObjectName("LogStart")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(680, 310, 61, 21))
        self.label_27.setObjectName("label_27")
        self.logfolder = QtWidgets.QLabel(Dialog)
        self.logfolder.setGeometry(QtCore.QRect(680, 340, 291, 21))
        self.logfolder.setText("")
        self.logfolder.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logfolder.setObjectName("logfolder")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(680, 150, 61, 21))
        self.label_28.setObjectName("label_28")
        self.ambT = QtWidgets.QLineEdit(Dialog)
        self.ambT.setGeometry(QtCore.QRect(760, 150, 51, 21))
        self.ambT.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ambT.setObjectName("ambT")
        self.setAmbT = QtWidgets.QPushButton(Dialog)
        self.setAmbT.setGeometry(QtCore.QRect(850, 150, 121, 21))
        self.setAmbT.setObjectName("setAmbT")
        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(820, 150, 21, 21))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(680, 180, 71, 21))
        self.label_30.setObjectName("label_30")
        self.dist = QtWidgets.QLineEdit(Dialog)
        self.dist.setGeometry(QtCore.QRect(760, 180, 51, 21))
        self.dist.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dist.setObjectName("dist")
        self.setDist = QtWidgets.QPushButton(Dialog)
        self.setDist.setGeometry(QtCore.QRect(850, 180, 121, 21))
        self.setDist.setObjectName("setDist")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(820, 180, 21, 21))
        self.label_31.setObjectName("label_31")
        self.rh = QtWidgets.QLineEdit(Dialog)
        self.rh.setGeometry(QtCore.QRect(760, 210, 51, 21))
        self.rh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rh.setObjectName("rh")
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(820, 210, 21, 21))
        self.label_32.setObjectName("label_32")
        self.setRH = QtWidgets.QPushButton(Dialog)
        self.setRH.setGeometry(QtCore.QRect(850, 210, 121, 21))
        self.setRH.setObjectName("setRH")
        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setGeometry(QtCore.QRect(680, 210, 71, 21))
        self.label_33.setObjectName("label_33")
        self.setEmissivity = QtWidgets.QPushButton(Dialog)
        self.setEmissivity.setGeometry(QtCore.QRect(850, 240, 121, 21))
        self.setEmissivity.setObjectName("setEmissivity")
        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setGeometry(QtCore.QRect(680, 240, 71, 21))
        self.label_34.setObjectName("label_34")
        self.emissivity = QtWidgets.QLineEdit(Dialog)
        self.emissivity.setGeometry(QtCore.QRect(760, 240, 51, 21))
        self.emissivity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.emissivity.setObjectName("emissivity")
        self.autofocusFull = QtWidgets.QPushButton(Dialog)
        self.autofocusFull.setGeometry(QtCore.QRect(680, 50, 91, 21))
        self.autofocusFull.setObjectName("autofocusFull")
        self.autofocusQuick = QtWidgets.QPushButton(Dialog)
        self.autofocusQuick.setGeometry(QtCore.QRect(770, 50, 101, 21))
        self.autofocusQuick.setObjectName("autofocusQuick")
        self.chooseFolderButton = QtWidgets.QPushButton(Dialog)
        self.chooseFolderButton.setGeometry(QtCore.QRect(770, 310, 201, 21))
        self.chooseFolderButton.setObjectName("chooseFolderButton")
        self.currentImg = QtWidgets.QLabel(Dialog)
        self.currentImg.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.currentImg.setText("")
        self.currentImg.setObjectName("currentImg")
        self.currentImg.raise_()
        self.flirIP.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.connect.raise_()
        self.label_22.raise_()
        self.line_5.raise_()
        self.label_20.raise_()
        self.atmT.raise_()
        self.setAtmT.raise_()
        self.shootNow.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.IntervalTime.raise_()
        self.IntervalSet.raise_()
        self.LogStart.raise_()
        self.label_27.raise_()
        self.logfolder.raise_()
        self.chooseFolderButton.raise_()
        self.label_28.raise_()
        self.ambT.raise_()
        self.setAmbT.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.dist.raise_()
        self.setDist.raise_()
        self.label_31.raise_()
        self.rh.raise_()
        self.label_32.raise_()
        self.setRH.raise_()
        self.label_33.raise_()
        self.setEmissivity.raise_()
        self.label_34.raise_()
        self.emissivity.raise_()
        self.autofocusFull.raise_()
        self.autofocusQuick.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FLIR A320 control"))
        Dialog.setWindowIcon(QtGui.QIcon('flir.png'))
        self.flirIP.setText(_translate("Dialog", "192.168.1.10"))
        self.label_2.setText(_translate("Dialog", "FLIR A320 IP:"))
        self.connect.setText(_translate("Dialog", "Connect"))
        self.label_22.setText(_translate("Dialog", "°C"))
        self.label_20.setText(_translate("Dialog", "Atm T:"))
        self.atmT.setText(_translate("Dialog", "-273.15"))
        self.setAtmT.setText(_translate("Dialog", "Set"))
        self.shootNow.setText(_translate("Dialog", "Shoot now"))
        self.label_25.setText(_translate("Dialog", "s"))
        self.label_26.setText(_translate("Dialog", "Interval:"))
        self.IntervalTime.setText(_translate("Dialog", "5"))
        self.IntervalSet.setText(_translate("Dialog", "Set interval"))
        self.LogStart.setText(_translate("Dialog", "Start logging"))
        self.label_27.setText(_translate("Dialog", "Logging to:"))
        self.label_28.setText(_translate("Dialog", "Ambient T:"))
        self.ambT.setText(_translate("Dialog", "25"))
        self.setAmbT.setText(_translate("Dialog", "Set"))
        self.label_29.setText(_translate("Dialog", "°C"))
        self.label_30.setText(_translate("Dialog", "Object dist.:"))
        self.dist.setText(_translate("Dialog", "5"))
        self.setDist.setText(_translate("Dialog", "Set"))
        self.label_31.setText(_translate("Dialog", "m"))
        self.rh.setText(_translate("Dialog", "50"))
        self.label_32.setText(_translate("Dialog", "%"))
        self.setRH.setText(_translate("Dialog", "Set"))
        self.label_33.setText(_translate("Dialog", "Rel. humid.:"))
        self.setEmissivity.setText(_translate("Dialog", "Set"))
        self.label_34.setText(_translate("Dialog", "Emissivity:"))
        self.emissivity.setText(_translate("Dialog", "0.95"))
        self.autofocusFull.setText(_translate("Dialog", "Autofocus (full)"))
        self.autofocusQuick.setText(_translate("Dialog", "Autofocus (quick)"))
        self.chooseFolderButton.setText(_translate("Dialog", "Choose dir..."))

