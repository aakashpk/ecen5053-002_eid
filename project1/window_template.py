# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_template2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 361, 321))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_updateTime = QtWidgets.QLabel(self.tab)
        self.label_updateTime.setGeometry(QtCore.QRect(134, 201, 160, 20))
        self.label_updateTime.setObjectName("label_updateTime")
        self.label_RHunit = QtWidgets.QLabel(self.tab)
        self.label_RHunit.setGeometry(QtCore.QRect(120, 144, 71, 30))
        self.label_RHunit.setObjectName("label_RHunit")
        self.lcd_humidity = QtWidgets.QLCDNumber(self.tab)
        self.lcd_humidity.setGeometry(QtCore.QRect(20, 140, 91, 41))
        self.lcd_humidity.setObjectName("lcd_humidity")
        self.radioButton_degC = QtWidgets.QRadioButton(self.tab)
        self.radioButton_degC.setGeometry(QtCore.QRect(122, 54, 80, 30))
        self.radioButton_degC.setChecked(True)
        self.radioButton_degC.setObjectName("radioButton_degC")
        self.pushButton_Refresh = QtWidgets.QPushButton(self.tab)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.label_lastUpdate = QtWidgets.QLabel(self.tab)
        self.label_lastUpdate.setGeometry(QtCore.QRect(21, 201, 100, 20))
        self.label_lastUpdate.setObjectName("label_lastUpdate")
        self.label_temperature = QtWidgets.QLabel(self.tab)
        self.label_temperature.setGeometry(QtCore.QRect(20, 31, 141, 20))
        self.label_temperature.setObjectName("label_temperature")
        self.radioButton_degF = QtWidgets.QRadioButton(self.tab)
        self.radioButton_degF.setGeometry(QtCore.QRect(122, 77, 90, 30))
        self.radioButton_degF.setObjectName("radioButton_degF")
        self.lcd_temperature = QtWidgets.QLCDNumber(self.tab)
        self.lcd_temperature.setGeometry(QtCore.QRect(20, 60, 91, 41))
        self.lcd_temperature.setAutoFillBackground(False)
        self.lcd_temperature.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(170, 255, 255);\n"
"}")
        self.lcd_temperature.setObjectName("lcd_temperature")
        self.label_humidity = QtWidgets.QLabel(self.tab)
        self.label_humidity.setGeometry(QtCore.QRect(20, 111, 141, 20))
        self.label_humidity.setObjectName("label_humidity")
        self.tabWidget.addTab(self.tab, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.AlarmLimt = QtWidgets.QLabel(self.Settings)
        self.AlarmLimt.setGeometry(QtCore.QRect(22, 59, 170, 16))
        self.AlarmLimt.setObjectName("AlarmLimt")
        self.AlarmLimitIn = QtWidgets.QLineEdit(self.Settings)
        self.AlarmLimitIn.setGeometry(QtCore.QRect(210, 59, 71, 20))
        self.AlarmLimitIn.setObjectName("AlarmLimitIn")
        self.RefreshDelay = QtWidgets.QLabel(self.Settings)
        self.RefreshDelay.setGeometry(QtCore.QRect(22, 98, 150, 16))
        self.RefreshDelay.setObjectName("RefreshDelay")
        self.RefreshDelIn = QtWidgets.QLineEdit(self.Settings)
        self.RefreshDelIn.setGeometry(QtCore.QRect(210, 98, 71, 20))
        self.RefreshDelIn.setObjectName("RefreshDelIn")
        self.PhNoIn = QtWidgets.QLineEdit(self.Settings)
        self.PhNoIn.setGeometry(QtCore.QRect(210, 135, 120, 20))
        self.PhNoIn.setObjectName("PhNoIn")
        self.phno = QtWidgets.QLabel(self.Settings)
        self.phno.setGeometry(QtCore.QRect(22, 135, 150, 16))
        self.phno.setObjectName("phno")
        self.ServiceProvider = QtWidgets.QLabel(self.Settings)
        self.ServiceProvider.setGeometry(QtCore.QRect(22, 171, 150, 16))
        self.ServiceProvider.setObjectName("ServiceProvider")
        self.phCoIn = QtWidgets.QComboBox(self.Settings)
        self.phCoIn.setGeometry(QtCore.QRect(210, 170, 111, 22))
        self.phCoIn.setObjectName("phCoIn")
        self.label = QtWidgets.QLabel(self.Settings)
        self.label.setGeometry(QtCore.QRect(289, 58, 50, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Settings)
        self.label_2.setGeometry(QtCore.QRect(290, 98, 60, 20))
        self.label_2.setObjectName("label_2")
        self.saveButton = QtWidgets.QPushButton(self.Settings)
        self.saveButton.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.tabWidget.addTab(self.Settings, "")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project_1_5053-002"))
        self.label_updateTime.setText(_translate("MainWindow", "Date Time"))
        self.label_RHunit.setText(_translate("MainWindow", "%RH"))
        self.radioButton_degC.setText(_translate("MainWindow", "degC"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_lastUpdate.setText(_translate("MainWindow", "Last Updated:"))
        self.label_temperature.setText(_translate("MainWindow", "Temperature"))
        self.radioButton_degF.setText(_translate("MainWindow", "degF"))
        self.label_humidity.setText(_translate("MainWindow", "Humidity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Display"))
        self.AlarmLimt.setText(_translate("MainWindow", "Temperature Alarm limit"))
        self.AlarmLimitIn.setText(_translate("MainWindow", "28"))
        self.RefreshDelay.setText(_translate("MainWindow", "Auto Refresh Delay"))
        self.RefreshDelIn.setText(_translate("MainWindow", "1"))
        self.PhNoIn.setText(_translate("MainWindow", "7202298666"))
        self.phno.setText(_translate("MainWindow", "Phone Number"))
        self.ServiceProvider.setText(_translate("MainWindow", "Service Provider"))
        self.label.setText(_translate("MainWindow", "degC"))
        self.label_2.setText(_translate("MainWindow", "minutes"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
