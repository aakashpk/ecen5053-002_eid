# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:13:09 2017

@author: Aakash
"""
import sys
import threading
from PyQt5.QtWidgets import QApplication, QDialog
from datetime import datetime
from window_template import Ui_MainWindow


import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 4
update_interval=1
unit=0

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()

def change_to_degF():
    global unit
    unit =1
    update_data()

def change_to_degC():
    global unit
    unit =0
    update_data()

ui.radioButton_degF.clicked.connect(lambda:change_to_degF())
ui.radioButton_degC.clicked.connect(lambda:change_to_degC())

def update_data(): # function to update temp and humidity data on display
    global update_interval
    global unit
    threading.Timer(60*update_interval,update_data).start() # to autorun function once every update interval
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    time=datetime.now().strftime('%b-%d-%Y %H:%M:%S')
    
    if(unit==1): # if unit is set to degF convert value to degF
        temperature=(temperature*1.8)+32 
    
    if(temperature==None): # handling data not being sent
        ui.lcd_temperature.display("Err")
    else:
        ui.lcd_temperature.display(temperature)
   
    if(humidity==None): # handling data not being sent
        ui.lcd_humidity.display("Err")
    else:
        ui.lcd_humidity.display(humidity)
    ui.label_updateTime.setText(time)

update_data()
ui.pushButton_Refresh.clicked.connect(lambda:update_data())

sys.exit(app.exec_())

