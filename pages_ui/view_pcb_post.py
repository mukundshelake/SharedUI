# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_pcb_post.ui'
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
        self.pbGoModule1 = QtWidgets.QPushButton(Form)
        self.pbGoModule1.setGeometry(QtCore.QRect(230, 160, 51, 21))
        self.pbGoModule1.setObjectName("pbGoModule1")
        self.pbGoModule2 = QtWidgets.QPushButton(Form)
        self.pbGoModule2.setGeometry(QtCore.QRect(230, 180, 51, 21))
        self.pbGoModule2.setObjectName("pbGoModule2")
        self.pbGoModule3 = QtWidgets.QPushButton(Form)
        self.pbGoModule3.setGeometry(QtCore.QRect(230, 200, 51, 21))
        self.pbGoModule3.setObjectName("pbGoModule3")
        self.pbGoModule4 = QtWidgets.QPushButton(Form)
        self.pbGoModule4.setGeometry(QtCore.QRect(230, 260, 51, 21))
        self.pbGoModule4.setObjectName("pbGoModule4")
        self.pbGoModule5 = QtWidgets.QPushButton(Form)
        self.pbGoModule5.setGeometry(QtCore.QRect(230, 220, 51, 21))
        self.pbGoModule5.setObjectName("pbGoModule5")
        self.pbGoModule6 = QtWidgets.QPushButton(Form)
        self.pbGoModule6.setGeometry(QtCore.QRect(230, 240, 51, 21))
        self.pbGoModule6.setObjectName("pbGoModule6")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(10, 140, 71, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(90, 140, 191, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 160, 71, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(10, 180, 71, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(10, 200, 71, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(10, 220, 71, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 240, 71, 20))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(10, 260, 71, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(770, 222, 131, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pbEdit = QtWidgets.QPushButton(Form)
        self.pbEdit.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(770, 190, 131, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pbSave = QtWidgets.QPushButton(Form)
        self.pbSave.setGeometry(QtCore.QRect(90, 40, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pbCancel = QtWidgets.QPushButton(Form)
        self.pbCancel.setGeometry(QtCore.QRect(170, 40, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setGeometry(QtCore.QRect(10, 500, 61, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.listIssues = QtWidgets.QListWidget(Form)
        self.listIssues.setGeometry(QtCore.QRect(10, 330, 721, 171))
        self.listIssues.setObjectName("listIssues")
        self.leStatus = QtWidgets.QLineEdit(Form)
        self.leStatus.setGeometry(QtCore.QRect(70, 500, 171, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.lineEdit_25 = QtWidgets.QLineEdit(Form)
        self.lineEdit_25.setGeometry(QtCore.QRect(10, 80, 151, 20))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.leModule5 = QtWidgets.QLineEdit(Form)
        self.leModule5.setGeometry(QtCore.QRect(90, 240, 141, 20))
        self.leModule5.setObjectName("leModule5")
        self.leModule1 = QtWidgets.QLineEdit(Form)
        self.leModule1.setGeometry(QtCore.QRect(90, 160, 141, 20))
        self.leModule1.setObjectName("leModule1")
        self.leModule2 = QtWidgets.QLineEdit(Form)
        self.leModule2.setGeometry(QtCore.QRect(90, 180, 141, 20))
        self.leModule2.setObjectName("leModule2")
        self.leModule4 = QtWidgets.QLineEdit(Form)
        self.leModule4.setGeometry(QtCore.QRect(90, 220, 141, 20))
        self.leModule4.setObjectName("leModule4")
        self.leModule3 = QtWidgets.QLineEdit(Form)
        self.leModule3.setGeometry(QtCore.QRect(90, 200, 141, 20))
        self.leModule3.setObjectName("leModule3")
        self.leModule6 = QtWidgets.QLineEdit(Form)
        self.leModule6.setGeometry(QtCore.QRect(90, 260, 141, 20))
        self.leModule6.setObjectName("leModule6")
        self.sbID = QtWidgets.QSpinBox(Form)
        self.sbID.setGeometry(QtCore.QRect(100, 10, 61, 21))
        self.sbID.setObjectName("sbID")
        self.cbInstitution = QtWidgets.QComboBox(Form)
        self.cbInstitution.setGeometry(QtCore.QRect(160, 80, 91, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.sbCureHumidity = QtWidgets.QSpinBox(Form)
        self.sbCureHumidity.setGeometry(QtCore.QRect(900, 220, 91, 26))
        self.sbCureHumidity.setProperty("value", 10)
        self.sbCureHumidity.setObjectName("sbCureHumidity")
        self.dsbCureTemperature = QtWidgets.QDoubleSpinBox(Form)
        self.dsbCureTemperature.setGeometry(QtCore.QRect(900, 188, 91, 26))
        self.dsbCureTemperature.setProperty("value", 70.0)
        self.dsbCureTemperature.setObjectName("dsbCureTemperature")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(770, 120, 101, 17))
        self.label_3.setObjectName("label_3")
        self.pbCureStartNow = QtWidgets.QPushButton(Form)
        self.pbCureStartNow.setGeometry(QtCore.QRect(990, 140, 91, 21))
        self.pbCureStartNow.setObjectName("pbCureStartNow")
        self.dtCureStart = QtWidgets.QDateTimeEdit(Form)
        self.dtCureStart.setGeometry(QtCore.QRect(840, 140, 151, 21))
        self.dtCureStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtCureStart.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtCureStart.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtCureStart.setCalendarPopup(True)
        self.dtCureStart.setObjectName("dtCureStart")
        self.lineEdit_28 = QtWidgets.QLineEdit(Form)
        self.lineEdit_28.setGeometry(QtCore.QRect(770, 140, 71, 21))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.pbCureStopNow = QtWidgets.QPushButton(Form)
        self.pbCureStopNow.setGeometry(QtCore.QRect(990, 160, 91, 21))
        self.pbCureStopNow.setObjectName("pbCureStopNow")
        self.dtCureStop = QtWidgets.QDateTimeEdit(Form)
        self.dtCureStop.setGeometry(QtCore.QRect(840, 160, 151, 21))
        self.dtCureStop.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtCureStop.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtCureStop.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtCureStop.setCalendarPopup(True)
        self.dtCureStop.setObjectName("dtCureStop")
        self.lineEdit_29 = QtWidgets.QLineEdit(Form)
        self.lineEdit_29.setGeometry(QtCore.QRect(770, 160, 71, 21))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.dsbOffX4 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffX4.setGeometry(QtCore.QRect(290, 220, 71, 21))
        self.dsbOffX4.setReadOnly(False)
        self.dsbOffX4.setMinimum(-1000.0)
        self.dsbOffX4.setMaximum(1000.0)
        self.dsbOffX4.setSingleStep(0.01)
        self.dsbOffX4.setObjectName("dsbOffX4")
        self.dsbOffX6 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffX6.setGeometry(QtCore.QRect(290, 260, 71, 21))
        self.dsbOffX6.setReadOnly(False)
        self.dsbOffX6.setMinimum(-1000.0)
        self.dsbOffX6.setMaximum(1000.0)
        self.dsbOffX6.setSingleStep(0.01)
        self.dsbOffX6.setObjectName("dsbOffX6")
        self.dsbOffX2 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffX2.setGeometry(QtCore.QRect(290, 180, 71, 21))
        self.dsbOffX2.setReadOnly(False)
        self.dsbOffX2.setMinimum(-1000.0)
        self.dsbOffX2.setMaximum(1000.0)
        self.dsbOffX2.setSingleStep(0.01)
        self.dsbOffX2.setObjectName("dsbOffX2")
        self.dsbOffRot5 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffRot5.setGeometry(QtCore.QRect(430, 240, 71, 21))
        self.dsbOffRot5.setReadOnly(False)
        self.dsbOffRot5.setMinimum(-180.0)
        self.dsbOffRot5.setMaximum(180.0)
        self.dsbOffRot5.setSingleStep(0.1)
        self.dsbOffRot5.setObjectName("dsbOffRot5")
        self.lineEdit_22 = QtWidgets.QLineEdit(Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(430, 140, 71, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.dsbOffY2 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffY2.setGeometry(QtCore.QRect(360, 180, 71, 21))
        self.dsbOffY2.setReadOnly(False)
        self.dsbOffY2.setMinimum(-1000.0)
        self.dsbOffY2.setMaximum(1000.0)
        self.dsbOffY2.setSingleStep(0.01)
        self.dsbOffY2.setObjectName("dsbOffY2")
        self.lineEdit_24 = QtWidgets.QLineEdit(Form)
        self.lineEdit_24.setGeometry(QtCore.QRect(360, 140, 71, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.dsbOffRot2 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffRot2.setGeometry(QtCore.QRect(430, 180, 71, 21))
        self.dsbOffRot2.setReadOnly(False)
        self.dsbOffRot2.setMinimum(-180.0)
        self.dsbOffRot2.setMaximum(180.0)
        self.dsbOffRot2.setSingleStep(0.1)
        self.dsbOffRot2.setObjectName("dsbOffRot2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(290, 120, 161, 17))
        self.label_4.setObjectName("label_4")
        self.dsbOffRot3 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffRot3.setGeometry(QtCore.QRect(430, 200, 71, 21))
        self.dsbOffRot3.setReadOnly(False)
        self.dsbOffRot3.setMinimum(-180.0)
        self.dsbOffRot3.setMaximum(180.0)
        self.dsbOffRot3.setSingleStep(0.1)
        self.dsbOffRot3.setObjectName("dsbOffRot3")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(290, 140, 71, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.dsbOffY4 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffY4.setGeometry(QtCore.QRect(360, 220, 71, 21))
        self.dsbOffY4.setReadOnly(False)
        self.dsbOffY4.setMinimum(-1000.0)
        self.dsbOffY4.setMaximum(1000.0)
        self.dsbOffY4.setSingleStep(0.01)
        self.dsbOffY4.setObjectName("dsbOffY4")
        self.dsbOffX3 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffX3.setGeometry(QtCore.QRect(290, 200, 71, 21))
        self.dsbOffX3.setReadOnly(False)
        self.dsbOffX3.setMinimum(-1000.0)
        self.dsbOffX3.setMaximum(1000.0)
        self.dsbOffX3.setSingleStep(0.01)
        self.dsbOffX3.setObjectName("dsbOffX3")
        self.dsbOffX1 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffX1.setGeometry(QtCore.QRect(290, 160, 71, 21))
        self.dsbOffX1.setReadOnly(False)
        self.dsbOffX1.setMinimum(-1000.0)
        self.dsbOffX1.setMaximum(1000.0)
        self.dsbOffX1.setSingleStep(0.01)
        self.dsbOffX1.setObjectName("dsbOffX1")
        self.dsbOffRot6 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffRot6.setGeometry(QtCore.QRect(430, 260, 71, 21))
        self.dsbOffRot6.setReadOnly(False)
        self.dsbOffRot6.setMinimum(-180.0)
        self.dsbOffRot6.setMaximum(180.0)
        self.dsbOffRot6.setSingleStep(0.1)
        self.dsbOffRot6.setObjectName("dsbOffRot6")
        self.dsbOffRot1 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffRot1.setGeometry(QtCore.QRect(430, 160, 71, 21))
        self.dsbOffRot1.setReadOnly(False)
        self.dsbOffRot1.setMinimum(-180.0)
        self.dsbOffRot1.setMaximum(180.0)
        self.dsbOffRot1.setSingleStep(0.1)
        self.dsbOffRot1.setObjectName("dsbOffRot1")
        self.dsbOffX5 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffX5.setGeometry(QtCore.QRect(290, 240, 71, 21))
        self.dsbOffX5.setReadOnly(False)
        self.dsbOffX5.setMinimum(-1000.0)
        self.dsbOffX5.setMaximum(1000.0)
        self.dsbOffX5.setSingleStep(0.01)
        self.dsbOffX5.setObjectName("dsbOffX5")
        self.dsbOffY6 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffY6.setGeometry(QtCore.QRect(360, 260, 71, 21))
        self.dsbOffY6.setReadOnly(False)
        self.dsbOffY6.setMinimum(-1000.0)
        self.dsbOffY6.setMaximum(1000.0)
        self.dsbOffY6.setSingleStep(0.01)
        self.dsbOffY6.setObjectName("dsbOffY6")
        self.dsbOffY5 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffY5.setGeometry(QtCore.QRect(360, 240, 71, 21))
        self.dsbOffY5.setReadOnly(False)
        self.dsbOffY5.setMinimum(-1000.0)
        self.dsbOffY5.setMaximum(1000.0)
        self.dsbOffY5.setSingleStep(0.01)
        self.dsbOffY5.setObjectName("dsbOffY5")
        self.dsbOffY3 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffY3.setGeometry(QtCore.QRect(360, 200, 71, 21))
        self.dsbOffY3.setReadOnly(False)
        self.dsbOffY3.setMinimum(-1000.0)
        self.dsbOffY3.setMaximum(1000.0)
        self.dsbOffY3.setSingleStep(0.01)
        self.dsbOffY3.setObjectName("dsbOffY3")
        self.dsbOffY1 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffY1.setGeometry(QtCore.QRect(360, 160, 71, 21))
        self.dsbOffY1.setReadOnly(False)
        self.dsbOffY1.setMinimum(-1000.0)
        self.dsbOffY1.setMaximum(1000.0)
        self.dsbOffY1.setSingleStep(0.01)
        self.dsbOffY1.setObjectName("dsbOffY1")
        self.dsbOffRot4 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbOffRot4.setGeometry(QtCore.QRect(430, 220, 71, 21))
        self.dsbOffRot4.setReadOnly(False)
        self.dsbOffRot4.setMinimum(-180.0)
        self.dsbOffRot4.setMaximum(180.0)
        self.dsbOffRot4.setSingleStep(0.1)
        self.dsbOffRot4.setObjectName("dsbOffRot4")
        self.lineEdit_23 = QtWidgets.QLineEdit(Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(510, 140, 81, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.dsbFlatness2 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbFlatness2.setGeometry(QtCore.QRect(510, 180, 81, 21))
        self.dsbFlatness2.setReadOnly(False)
        self.dsbFlatness2.setMinimum(-10.0)
        self.dsbFlatness2.setMaximum(10.0)
        self.dsbFlatness2.setSingleStep(0.1)
        self.dsbFlatness2.setObjectName("dsbFlatness2")
        self.dsbFlatness6 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbFlatness6.setGeometry(QtCore.QRect(510, 260, 81, 21))
        self.dsbFlatness6.setReadOnly(False)
        self.dsbFlatness6.setMinimum(-10.0)
        self.dsbFlatness6.setMaximum(10.0)
        self.dsbFlatness6.setSingleStep(0.1)
        self.dsbFlatness6.setObjectName("dsbFlatness6")
        self.dsbThickness3 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbThickness3.setGeometry(QtCore.QRect(590, 200, 81, 21))
        self.dsbThickness3.setReadOnly(False)
        self.dsbThickness3.setMinimum(-1.0)
        self.dsbThickness3.setMaximum(100.0)
        self.dsbThickness3.setSingleStep(0.1)
        self.dsbThickness3.setObjectName("dsbThickness3")
        self.dsbThickness2 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbThickness2.setGeometry(QtCore.QRect(590, 180, 81, 21))
        self.dsbThickness2.setReadOnly(False)
        self.dsbThickness2.setMinimum(-1.0)
        self.dsbThickness2.setMaximum(100.0)
        self.dsbThickness2.setSingleStep(0.1)
        self.dsbThickness2.setObjectName("dsbThickness2")
        self.lineEdit_30 = QtWidgets.QLineEdit(Form)
        self.lineEdit_30.setGeometry(QtCore.QRect(590, 140, 81, 21))
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.dsbFlatness5 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbFlatness5.setGeometry(QtCore.QRect(510, 240, 81, 21))
        self.dsbFlatness5.setReadOnly(False)
        self.dsbFlatness5.setMinimum(-10.0)
        self.dsbFlatness5.setMaximum(10.0)
        self.dsbFlatness5.setSingleStep(0.1)
        self.dsbFlatness5.setObjectName("dsbFlatness5")
        self.dsbThickness6 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbThickness6.setGeometry(QtCore.QRect(590, 260, 81, 21))
        self.dsbThickness6.setReadOnly(False)
        self.dsbThickness6.setMinimum(-1.0)
        self.dsbThickness6.setMaximum(100.0)
        self.dsbThickness6.setSingleStep(0.1)
        self.dsbThickness6.setObjectName("dsbThickness6")
        self.dsbThickness5 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbThickness5.setGeometry(QtCore.QRect(590, 240, 81, 21))
        self.dsbThickness5.setReadOnly(False)
        self.dsbThickness5.setMinimum(-1.0)
        self.dsbThickness5.setMaximum(100.0)
        self.dsbThickness5.setSingleStep(0.1)
        self.dsbThickness5.setObjectName("dsbThickness5")
        self.dsbFlatness3 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbFlatness3.setGeometry(QtCore.QRect(510, 200, 81, 21))
        self.dsbFlatness3.setReadOnly(False)
        self.dsbFlatness3.setMinimum(-10.0)
        self.dsbFlatness3.setMaximum(10.0)
        self.dsbFlatness3.setSingleStep(0.1)
        self.dsbFlatness3.setObjectName("dsbFlatness3")
        self.dsbFlatness1 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbFlatness1.setGeometry(QtCore.QRect(510, 160, 81, 21))
        self.dsbFlatness1.setReadOnly(False)
        self.dsbFlatness1.setMinimum(-10.0)
        self.dsbFlatness1.setMaximum(10.0)
        self.dsbFlatness1.setSingleStep(0.1)
        self.dsbFlatness1.setObjectName("dsbFlatness1")
        self.dsbFlatness4 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbFlatness4.setGeometry(QtCore.QRect(510, 220, 81, 21))
        self.dsbFlatness4.setReadOnly(False)
        self.dsbFlatness4.setMinimum(-10.0)
        self.dsbFlatness4.setMaximum(10.0)
        self.dsbFlatness4.setSingleStep(0.1)
        self.dsbFlatness4.setObjectName("dsbFlatness4")
        self.dsbThickness1 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbThickness1.setGeometry(QtCore.QRect(590, 160, 81, 21))
        self.dsbThickness1.setReadOnly(False)
        self.dsbThickness1.setMinimum(-1.0)
        self.dsbThickness1.setMaximum(100.0)
        self.dsbThickness1.setSingleStep(0.1)
        self.dsbThickness1.setObjectName("dsbThickness1")
        self.dsbThickness4 = QtWidgets.QDoubleSpinBox(Form)
        self.dsbThickness4.setGeometry(QtCore.QRect(590, 220, 81, 21))
        self.dsbThickness4.setReadOnly(False)
        self.dsbThickness4.setMinimum(-1.0)
        self.dsbThickness4.setMaximum(100.0)
        self.dsbThickness4.setSingleStep(0.1)
        self.dsbThickness4.setObjectName("dsbThickness4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(510, 120, 161, 17))
        self.label_5.setObjectName("label_5")
        self.cbGrade3 = QtWidgets.QComboBox(Form)
        self.cbGrade3.setEnabled(True)
        self.cbGrade3.setGeometry(QtCore.QRect(680, 200, 81, 20))
        self.cbGrade3.setObjectName("cbGrade3")
        self.cbGrade3.addItem("")
        self.cbGrade3.addItem("")
        self.cbGrade3.addItem("")
        self.cbGrade1 = QtWidgets.QComboBox(Form)
        self.cbGrade1.setEnabled(True)
        self.cbGrade1.setGeometry(QtCore.QRect(680, 160, 81, 20))
        self.cbGrade1.setObjectName("cbGrade1")
        self.cbGrade1.addItem("")
        self.cbGrade1.addItem("")
        self.cbGrade1.addItem("")
        self.cbGrade4 = QtWidgets.QComboBox(Form)
        self.cbGrade4.setEnabled(True)
        self.cbGrade4.setGeometry(QtCore.QRect(680, 220, 81, 20))
        self.cbGrade4.setObjectName("cbGrade4")
        self.cbGrade4.addItem("")
        self.cbGrade4.addItem("")
        self.cbGrade4.addItem("")
        self.cbGrade5 = QtWidgets.QComboBox(Form)
        self.cbGrade5.setEnabled(True)
        self.cbGrade5.setGeometry(QtCore.QRect(680, 240, 81, 20))
        self.cbGrade5.setObjectName("cbGrade5")
        self.cbGrade5.addItem("")
        self.cbGrade5.addItem("")
        self.cbGrade5.addItem("")
        self.lineEdit_31 = QtWidgets.QLineEdit(Form)
        self.lineEdit_31.setGeometry(QtCore.QRect(680, 140, 81, 21))
        self.lineEdit_31.setReadOnly(True)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(680, 120, 71, 17))
        self.label_6.setObjectName("label_6")
        self.cbGrade6 = QtWidgets.QComboBox(Form)
        self.cbGrade6.setEnabled(True)
        self.cbGrade6.setGeometry(QtCore.QRect(680, 260, 81, 20))
        self.cbGrade6.setObjectName("cbGrade6")
        self.cbGrade6.addItem("")
        self.cbGrade6.addItem("")
        self.cbGrade6.addItem("")
        self.cbGrade2 = QtWidgets.QComboBox(Form)
        self.cbGrade2.setEnabled(True)
        self.cbGrade2.setGeometry(QtCore.QRect(680, 180, 81, 20))
        self.cbGrade2.setObjectName("cbGrade2")
        self.cbGrade2.addItem("")
        self.cbGrade2.addItem("")
        self.cbGrade2.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 120, 161, 17))
        self.label_7.setObjectName("label_7")
        self.pbAddFile = QtWidgets.QPushButton(Form)
        self.pbAddFile.setGeometry(QtCore.QRect(290, 70, 101, 31))
        self.pbAddFile.setObjectName("pbAddFile")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(290, 20, 291, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_32 = QtWidgets.QLineEdit(Form)
        self.lineEdit_32.setGeometry(QtCore.QRect(290, 40, 101, 21))
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.leXML = QtWidgets.QLineEdit(Form)
        self.leXML.setEnabled(True)
        self.leXML.setGeometry(QtCore.QRect(390, 40, 181, 20))
        self.leXML.setReadOnly(True)
        self.leXML.setObjectName("leXML")

        self.retranslateUi(Form)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbGrade3.setCurrentIndex(-1)
        self.cbGrade1.setCurrentIndex(-1)
        self.cbGrade4.setCurrentIndex(-1)
        self.cbGrade5.setCurrentIndex(-1)
        self.cbGrade6.setCurrentIndex(-1)
        self.cbGrade2.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbGoModule1.setText(_translate("Form", "go to"))
        self.pbGoModule2.setText(_translate("Form", "go to"))
        self.pbGoModule3.setText(_translate("Form", "go to"))
        self.pbGoModule4.setText(_translate("Form", "go to"))
        self.pbGoModule5.setText(_translate("Form", "go to"))
        self.pbGoModule6.setText(_translate("Form", "go to"))
        self.lineEdit_12.setText(_translate("Form", "position"))
        self.lineEdit_14.setText(_translate("Form", "Module serial"))
        self.lineEdit_15.setText(_translate("Form", "1 (1, 1)"))
        self.lineEdit_16.setText(_translate("Form", "2 (1, 2)"))
        self.lineEdit_17.setText(_translate("Form", "3 (2, 1)"))
        self.lineEdit_18.setText(_translate("Form", "4 (2, 2)"))
        self.lineEdit_19.setText(_translate("Form", "5 (3, 1)"))
        self.lineEdit_20.setText(_translate("Form", "6 (3, 2)"))
        self.lineEdit_9.setText(_translate("Form", "cure humidity (%)"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.lineEdit_8.setText(_translate("Form", "cure temp (C)"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.lineEdit.setText(_translate("Form", "PCB step ID"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.lineEdit_26.setText(_translate("Form", "Status:"))
        self.listIssues.setToolTip(_translate("Form", "list of issues"))
        self.lineEdit_25.setText(_translate("Form", "Institution (for tools)"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.label_3.setText(_translate("Form", "Curing"))
        self.pbCureStartNow.setText(_translate("Form", "set to now"))
        self.lineEdit_28.setText(_translate("Form", "cure start"))
        self.pbCureStopNow.setText(_translate("Form", "set to now"))
        self.lineEdit_29.setText(_translate("Form", "cure stop"))
        self.lineEdit_22.setText(_translate("Form", "θ (°)"))
        self.lineEdit_24.setText(_translate("Form", "y (μm)"))
        self.label_4.setText(_translate("Form", "Placement offsets"))
        self.lineEdit_21.setText(_translate("Form", "x (μm)"))
        self.lineEdit_23.setText(_translate("Form", "Flat (mm)"))
        self.lineEdit_30.setText(_translate("Form", "Thick (mm)"))
        self.label_5.setText(_translate("Form", "Flatness & thickness"))
        self.cbGrade3.setItemText(0, _translate("Form", "A"))
        self.cbGrade3.setItemText(1, _translate("Form", "B"))
        self.cbGrade3.setItemText(2, _translate("Form", "C"))
        self.cbGrade1.setItemText(0, _translate("Form", "A"))
        self.cbGrade1.setItemText(1, _translate("Form", "B"))
        self.cbGrade1.setItemText(2, _translate("Form", "C"))
        self.cbGrade4.setItemText(0, _translate("Form", "A"))
        self.cbGrade4.setItemText(1, _translate("Form", "B"))
        self.cbGrade4.setItemText(2, _translate("Form", "C"))
        self.cbGrade5.setItemText(0, _translate("Form", "A"))
        self.cbGrade5.setItemText(1, _translate("Form", "B"))
        self.cbGrade5.setItemText(2, _translate("Form", "C"))
        self.lineEdit_31.setText(_translate("Form", "Grade"))
        self.label_6.setText(_translate("Form", "Quality"))
        self.cbGrade6.setItemText(0, _translate("Form", "A"))
        self.cbGrade6.setItemText(1, _translate("Form", "B"))
        self.cbGrade6.setItemText(2, _translate("Form", "C"))
        self.cbGrade2.setItemText(0, _translate("Form", "A"))
        self.cbGrade2.setItemText(1, _translate("Form", "B"))
        self.cbGrade2.setItemText(2, _translate("Form", "C"))
        self.label_7.setText(_translate("Form", "Part to cure"))
        self.pbAddFile.setText(_translate("Form", "Select file"))
        self.label_8.setText(_translate("Form", "Load assembly measurements from XML"))
        self.lineEdit_32.setText(_translate("Form", "Uploaded file"))
