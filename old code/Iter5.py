# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Iter4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT
from datetime import datetime
import sys

sensor = Adafruit_DHT.DHT22
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
updatetime=datetime.now().strftime('%b-%d-%Y %H:%M:%S')
#temp_f=((temperature*1.8)+32)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 49, 91, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        #self.lcdNumber.display(temperature)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 25, 141, 22))
        self.label.setObjectName("label")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(50, 129, 91, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 105, 141, 22))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 219, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.temp_humidity_update)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 139, 71, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(51, 190, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 190, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(151, 60, 90, 30))
        self.label_6.setObjectName("label_6")
        self.lcdNumber.raise_()
        self.label.raise_()
        self.lcdNumber_2.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.temp_humidity_update()
        #MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def temp_humidity_update(self):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        self.lcdNumber.display(temperature)
        self.lcdNumber_2.display(humidity)
        updatetime=datetime.now().strftime('%b-%d-%Y %H:%M:%S')
        self.label_5.setText(updatetime)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Reader v0"))
        self.label.setText(_translate("MainWindow", "Temperature"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.label_3.setText(_translate("MainWindow", "%RH"))
        self.label_4.setText(_translate("MainWindow", "Last Update:"))
        self.label_5.setText(_translate("MainWindow", updatetime))
        self.label_6.setText(_translate("MainWindow", "degC"))
          

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QDialog()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())