# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Iter3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
import Adafruit_DHT


sensor = Adafruit_DHT.DHT22
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

temp_f=((temperature*1.8)+32)
'''
if humidity is not None and temperature is not None:
   print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
'''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 60, 91, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(temperature)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 141, 16))
        self.label.setObjectName("label")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(50, 140, 91, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.display(humidity)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 141, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.temp_humidity_update)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 71, 16))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(151, 61, 71, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(151, 84, 81, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lcdNumber.raise_()
        self.label.raise_()
        self.lcdNumber_2.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def temp_humidity_update(self):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        self.lcdNumber.display(temperature)
        self.lcdNumber_2.display(humidity)
        self.label.setText(datetime.now())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Temperature"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.label_3.setText(_translate("MainWindow", "%RH"))
        self.radioButton.setText(_translate("MainWindow", "degC"))
        self.radioButton_2.setText(_translate("MainWindow", "degF"))
             
        
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QDialog()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
                

