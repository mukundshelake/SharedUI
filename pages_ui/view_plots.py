# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_plots.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1199, 756)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pbCancelPCB = QtWidgets.QPushButton(Form)
        self.pbCancelPCB.setGeometry(QtCore.QRect(100, 50, 81, 21))
        self.pbCancelPCB.setObjectName("pbCancelPCB")
        self.pbEditPCB = QtWidgets.QPushButton(Form)
        self.pbEditPCB.setGeometry(QtCore.QRect(160, 30, 81, 21))
        self.pbEditPCB.setObjectName("pbEditPCB")
        self.pbSavePCB = QtWidgets.QPushButton(Form)
        self.pbSavePCB.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.pbSavePCB.setObjectName("pbSavePCB")
        self.pbGoPCB = QtWidgets.QPushButton(Form)
        self.pbGoPCB.setGeometry(QtCore.QRect(240, 10, 61, 21))
        self.pbGoPCB.setObjectName("pbGoPCB")
        self.pteWriteCommentPCB = QtWidgets.QPlainTextEdit(Form)
        self.pteWriteCommentPCB.setGeometry(QtCore.QRect(10, 440, 351, 61))
        self.pteWriteCommentPCB.setPlainText("")
        self.pteWriteCommentPCB.setObjectName("pteWriteCommentPCB")
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(10, 320, 231, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pbDeleteCommentPCB = QtWidgets.QPushButton(Form)
        self.pbDeleteCommentPCB.setGeometry(QtCore.QRect(240, 320, 121, 21))
        self.pbDeleteCommentPCB.setObjectName("pbDeleteCommentPCB")
        self.listCommentsPCB = QtWidgets.QListWidget(Form)
        self.listCommentsPCB.setGeometry(QtCore.QRect(10, 340, 351, 91))
        self.listCommentsPCB.setObjectName("listCommentsPCB")
        self.pbAddCommentPCB = QtWidgets.QPushButton(Form)
        self.pbAddCommentPCB.setGeometry(QtCore.QRect(10, 500, 111, 21))
        self.pbAddCommentPCB.setObjectName("pbAddCommentPCB")
        self.leIDPCB = QtWidgets.QLineEdit(Form)
        self.leIDPCB.setGeometry(QtCore.QRect(130, 10, 111, 20))
        self.leIDPCB.setText("")
        self.leIDPCB.setReadOnly(True)
        self.leIDPCB.setObjectName("leIDPCB")
        self.leStatusPCB = QtWidgets.QLineEdit(Form)
        self.leStatusPCB.setGeometry(QtCore.QRect(190, 50, 111, 20))
        self.leStatusPCB.setText("")
        self.leStatusPCB.setReadOnly(True)
        self.leStatusPCB.setObjectName("leStatusPCB")
        self.pbLoadPCB = QtWidgets.QPushButton(Form)
        self.pbLoadPCB.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.pbLoadPCB.setObjectName("pbLoadPCB")
        self.pbDeleteFilesPCB = QtWidgets.QPushButton(Form)
        self.pbDeleteFilesPCB.setGeometry(QtCore.QRect(230, 120, 131, 21))
        self.pbDeleteFilesPCB.setObjectName("pbDeleteFilesPCB")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 241, 16))
        self.label_7.setObjectName("label_7")
        self.listFilesPCB = QtWidgets.QListWidget(Form)
        self.listFilesPCB.setGeometry(QtCore.QRect(10, 140, 351, 111))
        self.listFilesPCB.setObjectName("listFilesPCB")
        self.lineEdit_17 = QtWidgets.QLineEdit(Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(11, 120, 221, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pbAddFilesPCB = QtWidgets.QPushButton(Form)
        self.pbAddFilesPCB.setGeometry(QtCore.QRect(10, 260, 101, 31))
        self.pbAddFilesPCB.setObjectName("pbAddFilesPCB")
        self.listFilesMod = QtWidgets.QListWidget(Form)
        self.listFilesMod.setGeometry(QtCore.QRect(450, 140, 351, 111))
        self.listFilesMod.setObjectName("listFilesMod")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(450, 100, 241, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(451, 120, 221, 21))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pbAddFilesMod = QtWidgets.QPushButton(Form)
        self.pbAddFilesMod.setGeometry(QtCore.QRect(450, 260, 101, 31))
        self.pbAddFilesMod.setObjectName("pbAddFilesMod")
        self.pbDeleteFilesMod = QtWidgets.QPushButton(Form)
        self.pbDeleteFilesMod.setGeometry(QtCore.QRect(670, 120, 131, 21))
        self.pbDeleteFilesMod.setObjectName("pbDeleteFilesMod")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 10, 121, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pbGoMod = QtWidgets.QPushButton(Form)
        self.pbGoMod.setGeometry(QtCore.QRect(680, 10, 71, 21))
        self.pbGoMod.setObjectName("pbGoMod")
        self.leIDMod = QtWidgets.QLineEdit(Form)
        self.leIDMod.setGeometry(QtCore.QRect(570, 10, 111, 20))
        self.leIDMod.setText("")
        self.leIDMod.setReadOnly(True)
        self.leIDMod.setObjectName("leIDMod")
        self.pbLoadMod = QtWidgets.QPushButton(Form)
        self.pbLoadMod.setGeometry(QtCore.QRect(450, 30, 121, 21))
        self.pbLoadMod.setObjectName("pbLoadMod")
        self.pbSaveMod = QtWidgets.QPushButton(Form)
        self.pbSaveMod.setGeometry(QtCore.QRect(450, 50, 81, 21))
        self.pbSaveMod.setObjectName("pbSaveMod")
        self.leStatusMod = QtWidgets.QLineEdit(Form)
        self.leStatusMod.setGeometry(QtCore.QRect(630, 50, 121, 20))
        self.leStatusMod.setText("")
        self.leStatusMod.setReadOnly(True)
        self.leStatusMod.setObjectName("leStatusMod")
        self.pbEditMod = QtWidgets.QPushButton(Form)
        self.pbEditMod.setGeometry(QtCore.QRect(600, 30, 81, 21))
        self.pbEditMod.setObjectName("pbEditMod")
        self.pbCancelMod = QtWidgets.QPushButton(Form)
        self.pbCancelMod.setGeometry(QtCore.QRect(540, 50, 81, 21))
        self.pbCancelMod.setObjectName("pbCancelMod")
        self.pteWriteCommentMod = QtWidgets.QPlainTextEdit(Form)
        self.pteWriteCommentMod.setGeometry(QtCore.QRect(450, 440, 351, 61))
        self.pteWriteCommentMod.setPlainText("")
        self.pteWriteCommentMod.setObjectName("pteWriteCommentMod")
        self.pbAddCommentMod = QtWidgets.QPushButton(Form)
        self.pbAddCommentMod.setGeometry(QtCore.QRect(450, 500, 111, 21))
        self.pbAddCommentMod.setObjectName("pbAddCommentMod")
        self.listCommentsMod = QtWidgets.QListWidget(Form)
        self.listCommentsMod.setGeometry(QtCore.QRect(450, 340, 351, 91))
        self.listCommentsMod.setObjectName("listCommentsMod")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(450, 320, 231, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pbDeleteCommentMod = QtWidgets.QPushButton(Form)
        self.pbDeleteCommentMod.setGeometry(QtCore.QRect(680, 320, 121, 21))
        self.pbDeleteCommentMod.setObjectName("pbDeleteCommentMod")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "PCB ID"))
        self.pbCancelPCB.setText(_translate("Form", "Cancel"))
        self.pbEditPCB.setText(_translate("Form", "Edit"))
        self.pbSavePCB.setText(_translate("Form", "Save"))
        self.pbGoPCB.setText(_translate("Form", "Go to"))
        self.lineEdit_16.setText(_translate("Form", "PCB comments"))
        self.pbDeleteCommentPCB.setText(_translate("Form", "Delete selected"))
        self.pbAddCommentPCB.setText(_translate("Form", "Add comment"))
        self.pbLoadPCB.setText(_translate("Form", "Load / check DB"))
        self.pbDeleteFilesPCB.setText(_translate("Form", "Delete selected"))
        self.label_7.setText(_translate("Form", "PCB plots"))
        self.listFilesPCB.setToolTip(_translate("Form", "ID (date sent) (SENDER to RECEIVER)"))
        self.lineEdit_17.setText(_translate("Form", "PCB files"))
        self.pbAddFilesPCB.setText(_translate("Form", "Add files"))
        self.listFilesMod.setToolTip(_translate("Form", "ID (date sent) (SENDER to RECEIVER)"))
        self.label_8.setText(_translate("Form", "Module plots"))
        self.lineEdit_18.setText(_translate("Form", "Module files"))
        self.pbAddFilesMod.setText(_translate("Form", "Add files"))
        self.pbDeleteFilesMod.setText(_translate("Form", "Delete selected"))
        self.lineEdit_2.setText(_translate("Form", "Module ID"))
        self.pbGoMod.setText(_translate("Form", "Go to"))
        self.pbLoadMod.setText(_translate("Form", "Load / check DB"))
        self.pbSaveMod.setText(_translate("Form", "Save"))
        self.pbEditMod.setText(_translate("Form", "Edit"))
        self.pbCancelMod.setText(_translate("Form", "Cancel"))
        self.pbAddCommentMod.setText(_translate("Form", "Add comment"))
        self.lineEdit_19.setText(_translate("Form", "Module comments"))
        self.pbDeleteCommentMod.setText(_translate("Form", "Delete selected"))
