# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:30:24 2017

@author: Aakash
"""

import Adafruit_DHT
import threading
from datetime import datetime
import RPi.GPIO as gpio

sensor = Adafruit_DHT.DHT22
pin = 4
led= 26
gpio.setmode(gpio.BOARD)
gpio.setup(led,gpio.OUT,initial=gpio.HIGH)

temperature=26
humidity=51

def ledON():
    gpio.output(led,1)
    
def ledOff():
    gpio.output(led,0)

def getData():
    """ function to read sensor data"""
    global temperature,humidity
    threading.Timer(2,getData).start()
    
    ledOff()
    
    humidity, temperature=Adafruit_DHT.read_retry(sensor, pin,5,1)
    if(temperature==None):
        temperature=-99
        ledON() # turn on LED in case of sensor error
    if(humidity==None):
        humidity=-99
        ledON # turn ON led in case of sensor error
    print("data read at ",datetime.now(),": T is :",temperature,"H is: ",humidity)

def get_TempHum():
    """ Sensor data stored in global variable to prevent simultaneous call to
    sensor by multiple modules"""
    global temperature, humidity
    return humidity,temperature

    
def todegF(degc):
    return (degc*1.8)+32
