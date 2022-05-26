# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_shipment.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 705)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 261, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.pbShipmentSave = QtWidgets.QPushButton(self.frame_3)
        self.pbShipmentSave.setGeometry(QtCore.QRect(90, 30, 71, 21))
        self.pbShipmentSave.setObjectName("pbShipmentSave")
        self.pbShipmentEdit = QtWidgets.QPushButton(self.frame_3)
        self.pbShipmentEdit.setGeometry(QtCore.QRect(0, 50, 81, 21))
        self.pbShipmentEdit.setObjectName("pbShipmentEdit")
        self.pbShipmentCancel = QtWidgets.QPushButton(self.frame_3)
        self.pbShipmentCancel.setGeometry(QtCore.QRect(170, 30, 71, 21))
        self.pbShipmentCancel.setObjectName("pbShipmentCancel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(1, 1, 171, 19))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pbShipmentNew = QtWidgets.QPushButton(self.frame_3)
        self.pbShipmentNew.setGeometry(QtCore.QRect(0, 30, 81, 21))
        self.pbShipmentNew.setObjectName("pbShipmentNew")
        self.sbShipmentID = QtWidgets.QSpinBox(self.frame_3)
        self.sbShipmentID.setGeometry(QtCore.QRect(170, 1, 91, 20))
        self.sbShipmentID.setMaximum(2147483647)
        self.sbShipmentID.setObjectName("sbShipmentID")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 140, 71, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 160, 71, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.leSender = QtWidgets.QLineEdit(Form)
        self.leSender.setGeometry(QtCore.QRect(80, 140, 171, 20))
        self.leSender.setObjectName("leSender")
        self.leReceiver = QtWidgets.QLineEdit(Form)
        self.leReceiver.setGeometry(QtCore.QRect(80, 160, 171, 20))
        self.leReceiver.setObjectName("leReceiver")
        self.pbSentNow = QtWidgets.QPushButton(Form)
        self.pbSentNow.setGeometry(QtCore.QRect(470, 140, 91, 21))
        self.pbSentNow.setObjectName("pbSentNow")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 140, 111, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 160, 111, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pbReceivedNow = QtWidgets.QPushButton(Form)
        self.pbReceivedNow.setGeometry(QtCore.QRect(470, 160, 91, 21))
        self.pbReceivedNow.setObjectName("pbReceivedNow")
        self.cbPartType = QtWidgets.QComboBox(Form)
        self.cbPartType.setGeometry(QtCore.QRect(60, 610, 141, 21))
        self.cbPartType.setObjectName("cbPartType")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.cbPartType.addItem("")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 110, 111, 20))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.cbShipmentType = QtWidgets.QComboBox(Form)
        self.cbShipmentType.setGeometry(QtCore.QRect(120, 110, 131, 21))
        self.cbShipmentType.setObjectName("cbShipmentType")
        self.cbShipmentType.addItem("")
        self.cbShipmentType.addItem("")
        self.pbAddPart = QtWidgets.QPushButton(Form)
        self.pbAddPart.setGeometry(QtCore.QRect(10, 610, 51, 21))
        self.pbAddPart.setObjectName("pbAddPart")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 630, 51, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lwPartList = QtWidgets.QListWidget(Form)
        self.lwPartList.setGeometry(QtCore.QRect(10, 220, 311, 391))
        self.lwPartList.setObjectName("lwPartList")
        self.pbDeleteSelected = QtWidgets.QPushButton(Form)
        self.pbDeleteSelected.setGeometry(QtCore.QRect(10, 660, 151, 21))
        self.pbDeleteSelected.setObjectName("pbDeleteSelected")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 200, 191, 16))
        self.label.setObjectName("label")
        self.lwErrList = QtWidgets.QListWidget(Form)
        self.lwErrList.setGeometry(QtCore.QRect(350, 220, 371, 181))
        self.lwErrList.setObjectName("lwErrList")
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setGeometry(QtCore.QRect(350, 400, 61, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.leStatus = QtWidgets.QLineEdit(Form)
        self.leStatus.setGeometry(QtCore.QRect(410, 400, 171, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.pbGoToSelected = QtWidgets.QPushButton(Form)
        self.pbGoToSelected.setGeometry(QtCore.QRect(170, 660, 151, 21))
        self.pbGoToSelected.setObjectName("pbGoToSelected")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 200, 191, 16))
        self.label_2.setObjectName("label_2")
        self.leFedEx = QtWidgets.QLineEdit(Form)
        self.leFedEx.setGeometry(QtCore.QRect(340, 110, 131, 20))
        self.leFedEx.setObjectName("leFedEx")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(270, 110, 71, 20))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.dSent = QtWidgets.QDateEdit(Form)
        self.dSent.setGeometry(QtCore.QRect(380, 140, 91, 21))
        self.dSent.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dSent.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dSent.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dSent.setCalendarPopup(True)
        self.dSent.setObjectName("dSent")
        self.dReceived = QtWidgets.QDateEdit(Form)
        self.dReceived.setGeometry(QtCore.QRect(380, 160, 91, 21))
        self.dReceived.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dReceived.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dReceived.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dReceived.setCalendarPopup(True)
        self.dReceived.setObjectName("dReceived")
        self.lePartID = QtWidgets.QLineEdit(Form)
        self.lePartID.setGeometry(QtCore.QRect(60, 630, 141, 20))
        self.lePartID.setObjectName("lePartID")

        self.retranslateUi(Form)
        self.cbShipmentType.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbShipmentSave.setText(_translate("Form", "Save"))
        self.pbShipmentEdit.setText(_translate("Form", "Edit"))
        self.pbShipmentCancel.setText(_translate("Form", "Cancel"))
        self.lineEdit.setText(_translate("Form", "Shipment ID"))
        self.pbShipmentNew.setText(_translate("Form", "New"))
        self.lineEdit_2.setText(_translate("Form", "Sender"))
        self.lineEdit_3.setText(_translate("Form", "Receiver"))
        self.pbSentNow.setText(_translate("Form", "set to today"))
        self.lineEdit_4.setText(_translate("Form", "Date sent"))
        self.lineEdit_5.setText(_translate("Form", "Date Received"))
        self.pbReceivedNow.setText(_translate("Form", "set to today"))
        self.cbPartType.setItemText(0, _translate("Form", "module"))
        self.cbPartType.setItemText(1, _translate("Form", "baseplate"))
        self.cbPartType.setItemText(2, _translate("Form", "sensor"))
        self.cbPartType.setItemText(3, _translate("Form", "pcb"))
        self.cbPartType.setItemText(4, _translate("Form", "protomodule"))
        self.lineEdit_7.setText(_translate("Form", "Shipment type"))
        self.cbShipmentType.setItemText(0, _translate("Form", "sending parts"))
        self.cbShipmentType.setItemText(1, _translate("Form", "receiving parts"))
        self.pbAddPart.setText(_translate("Form", "add"))
        self.lineEdit_6.setText(_translate("Form", "serial"))
        self.pbDeleteSelected.setText(_translate("Form", "delete selected part"))
        self.label.setText(_translate("Form", "parts in shipment"))
        self.lineEdit_26.setText(_translate("Form", "Status:"))
        self.pbGoToSelected.setText(_translate("Form", "go to selected part"))
        self.label_2.setText(_translate("Form", "error list"))
        self.lineEdit_8.setText(_translate("Form", "FedEx ID"))
