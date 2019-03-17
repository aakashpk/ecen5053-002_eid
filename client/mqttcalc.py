from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import logging
import time
import argparse
import sqs_pull

from datetime import datetime

dbSamplingInterval=5

starttime=0
endtime=0
rtt=0

# Custom MQTT message callback
def customCallback(client, userdata, message):
    global starttime,endtime,rtt
    endtime=time.time()
    #print("Received a new message: ")
    rtt=endtime-starttime
    print("Start Time: ",starttime)
    print("End Time: ",endtime)
    print("Time Taken",rtt,"seconds")
    return rtt
    

#Paths for certificates
host = 'a3c1qeo00yd0b1.iot.us-west-2.amazonaws.com' 
rootCAPath = 'root-CA.crt' 
certificatePath = 'raspberry-pi.cert.pem' 
privateKeyPath = 'raspberry-pi.private.key' 
useWebsocket = False 
clientId = 'mqttClient' 
subtopic='proj4/rx'
pubtopic='proj4/tx'

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.NOTSET)  #logging.DEBUG
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


def publishMessage(message,topic):
    global starttime
    print("publish message")
    starttime=time.time()
    myAWSIoTMQTTClient.publish(topic, message, 0)    
    
def getMqttTime():
    queue,length=sqs_pull.getSqsQueue()
    print("getmqtt")
    publishMessage(str(queue),pubtopic)
    time.sleep(5)
    return rtt



# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(subtopic, 1, customCallback)

