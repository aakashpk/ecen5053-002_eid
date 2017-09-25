# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_template.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcd_temperature = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_temperature.setGeometry(QtCore.QRect(26, 49, 91, 41))
        self.lcd_temperature.setObjectName("lcd_temperature")
        self.label_temperature = QtWidgets.QLabel(self.centralwidget)
        self.label_temperature.setGeometry(QtCore.QRect(26, 20, 141, 20))
        self.label_temperature.setObjectName("label_temperature")
        self.lcd_humidity = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_humidity.setGeometry(QtCore.QRect(26, 129, 91, 41))
        self.lcd_humidity.setObjectName("lcd_humidity")
        self.label_humidity = QtWidgets.QLabel(self.centralwidget)
        self.label_humidity.setGeometry(QtCore.QRect(26, 100, 141, 20))
        self.label_humidity.setObjectName("label_humidity")
        self.pushButton_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(26, 219, 75, 23))
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.label_RHunit = QtWidgets.QLabel(self.centralwidget)
        self.label_RHunit.setGeometry(QtCore.QRect(126, 133, 71, 30))
        self.label_RHunit.setObjectName("label_RHunit")
        self.label_lastUpdate = QtWidgets.QLabel(self.centralwidget)
        self.label_lastUpdate.setGeometry(QtCore.QRect(27, 190, 100, 20))
        self.label_lastUpdate.setObjectName("label_lastUpdate")
        self.label_updateTime = QtWidgets.QLabel(self.centralwidget)
        self.label_updateTime.setGeometry(QtCore.QRect(140, 190, 160, 20))
        self.label_updateTime.setObjectName("label_updateTime")
        self.radioButton_degC = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_degC.setGeometry(QtCore.QRect(128, 43, 80, 30))
        self.radioButton_degC.setChecked(True)
        self.radioButton_degC.setObjectName("radioButton_degC")
        self.radioButton_degF = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_degF.setGeometry(QtCore.QRect(128, 66, 90, 30))
        self.radioButton_degF.setObjectName("radioButton_degF")
        self.lcd_temperature.raise_()
        self.label_temperature.raise_()
        self.lcd_humidity.raise_()
        self.label_humidity.raise_()
        self.pushButton_Refresh.raise_()
        self.label_RHunit.raise_()
        self.radioButton_degC.raise_()
        self.radioButton_degF.raise_()
        self.label_lastUpdate.raise_()
        self.label_updateTime.raise_()
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project_1_5053-002"))
        self.label_temperature.setText(_translate("MainWindow", "Temperature"))
        self.label_humidity.setText(_translate("MainWindow", "Humidity"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_RHunit.setText(_translate("MainWindow", "%RH"))
        self.label_lastUpdate.setText(_translate("MainWindow", "Last Updated:"))
        self.label_updateTime.setText(_translate("MainWindow", "Date Time"))
        self.radioButton_degC.setText(_translate("MainWindow", "degC"))
        self.radioButton_degF.setText(_translate("MainWindow", "degF"))

