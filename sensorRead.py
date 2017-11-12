# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:30:24 2017

@author: Aakash
"""

import Adafruit_DHT
import threading
from datetime import datetime

sensor = Adafruit_DHT.DHT22
pin = 4

temperature=25
humidity=50

def getData():
    global temperature,humidity
    threading.Timer(2,getData).start()

    humidity, temperature=Adafruit_DHT.read_retry(sensor, pin,5,1)
    if(temperature==None):
        temperature=-99
    if(humidity==None):
        humidity=-99
    print("data read at ",datetime.now(),": T is :",temperature,"H is: ",humidity)

def get_TempHum():
    global temperature, humidity
    return humidity,temperature

def todegF(degc):
    return (degc*1.8)+32
