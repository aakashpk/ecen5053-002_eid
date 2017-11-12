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

def getData():
    threading.Timer(2,getData).start()
    temperature, humidity=Adafruit_DHT.read_retry(sensor, pin)
    print("data read at ",datetime.now(),": T is :",temperature,"H is: ",humidity)

def get_TempHum():
    global temperature, humidity
    return temperature, humidity

def todegF(degc):
    return (degc*1.8)+32