'''
/*
 * Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import logging
import time
import argparse
import sensorRead
import databaseOps
from datetime import datetime
import threading

dbSamplingInterval=5
sensorRead.getData()
databaseOps.purgeDb()
databaseOps.addDataToDb()

# Custom MQTT message callback
def customCallback(client, userdata, message):
	#print("Received a new message: ")
	print(message.payload)
	print(" topic: ")
	print(message.topic)
	#print("--------------\n\n")

#Paths for certificates
host = 'aws-client-id' 
rootCAPath = 'root-CA.crt' 
certificatePath = 'raspberry-pi.cert.pem' 
privateKeyPath = 'raspberry-pi.private.key' 
useWebsocket = False 
clientId = 'basicPubSub' 
topic='proj3/rpi'

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.INFO)  #logging.DEBUG
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
if useWebsocket:
	myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
	myAWSIoTMQTTClient.configureEndpoint(host, 443)
	myAWSIoTMQTTClient.configureCredentials(rootCAPath)
else:
	myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
	myAWSIoTMQTTClient.configureEndpoint(host, 8883)
	myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)

def publishTempHumidity():
    """" Function to publish temp and humidity data to AWS using MQTT"""
    global dbSamplingInterval,topic
    threading.Timer(dbSamplingInterval,publishTempHumidity).start() # to autorun function once every update interval
    ts=datetime.now()
    h,t= sensorRead.get_TempHum()
    msg = '"ts": "{}", "Temperature": "{}", "Humidity": "{}"'.format(ts, t,h)
    msg = '{'+msg+'}'
    myAWSIoTMQTTClient.publish(topic, msg, 1)

publishTempHumidity() # send temperature and humidity
