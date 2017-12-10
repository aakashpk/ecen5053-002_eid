# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 23:24:44 2017

@author: Aakash
"""

import mqttcalc
import client_coap
import asyncio

"""
import sqs_pull
import time

pubtopic='proj4/tx'

queue,length=sqs_pull.getSqsQueue()


mqttcalc.publishMessage(str(queue),pubtopic)

time.sleep(5)
"""
print("MQTT time")
print(mqttcalc.getMqttTime())

print("CoAP time")
print(asyncio.get_event_loop().run_until_complete(client_coap.coap_response()))