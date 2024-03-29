import sys
import json
import datetime
import boto3
import matplotlib.pyplot as plt
import mqttcalc
import client_coap
import asyncio
import sqs_pull
import ws_client
from datetime import datetime
import time
import amqp_send

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *



def QT():
    global t1
    ##### Creating an object for the application ################
    app = QApplication(sys.argv)
    ####### Declaring Tabs ########################################
    tabs = QtGui.QTabWidget()
    tab1 = QtGui.QWidget()
    tab2 = QtGui.QWidget()
    tabs.resize (1700, 1700)
    ####### Setting a Window Title ################################
    tabs.setWindowTitle("Temperature and Humidity")
    ######  Creating Vertical Box layout for tab1  ################
    vBoxlayout = QtGui.QVBoxLayout()
    tab1.setLayout(vBoxlayout)
    ####### Creating Vertical Box Layout for tab2  ################
    vBoxlayout = QtGui.QVBoxLayout()
    tab2.setLayout(vBoxlayout)
    ######## Adding names for tab1 and tab2 ########################
    tabs.addTab(tab1,"Temperature")
    tabs.addTab(tab2,"Humidity")
    ######## Creating label for tab1 ################################
    t1 = QLabel(tab1)
    t1.move(100,140)
    ################### Creating buttons for tab1####################
    button1 = QPushButton(tab1)
    button2 = QPushButton(tab1)
    button3 = QPushButton(tab1)
    button4 = QPushButton(tab1)
    
    ################### Creating buttons for tab2####################
    b1 = QPushButton(tab2)
    b2 = QPushButton(tab2)
    b3 = QPushButton(tab2)
    ################## Names of buttons in tab1 ###########################
    button1.setText("Data Request")
    button1.move(300,100)
    button2.setText("CtoF")
    button2.move(300,300)
    button3.setText("SQS  Check")
    button3.move(100,100)
    button4.setText("Protocol Test")
    button4.move(100,200)
    
    ################### Button 2 #################################
    b1.setText("Data Request")
    b1.move(300,100)
    b2.setText("Quit")
    b2.move(300,300)
    b3.setText("Protocol Test")
    b3.move(300,400)
    ############## Defining actions for buttons ##################
    button1.clicked.connect(button1_clicked)
    button2.clicked.connect(button2_clicked)
    button3.clicked.connect(button3_clicked)
    button4.clicked.connect(button4_clicked)

    b1.clicked.connect(b1_clicked)
    b2.clicked.connect(b2_clicked)
    b3.clicked.connect(b3_clicked)
    tabs.show()
    sys.exit(app.exec_())

def button1_clicked():
    print('Pull Data Request button for Temperature is clicked')
    sqs = boto3.client('sqs', region_name='us-west-2',
                   aws_access_key_id = 'AKIAJNQ4FNHFZP437GIQ',
                   aws_secret_access_key = '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')
    #printing queue url

    url = sqs.get_queue_url(QueueName='proj3_data_sqs')
    print(url['QueueUrl'])
    # Receiving messages from SQS queue

    response = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response1 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response2 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response['Messages'] = (response['Messages'] + response1['Messages'] + response2['Messages'])
    for i in range (0,30):
         message = response['Messages'][i]
         #Spliting string and taking timestamp value
         body = response['Messages'][i]['Body']
         print('\n The body content is %s' %body)
         x = body.split(",")
         print('\n The sliced string is %s' %x[0])
         a = float(x[1])
         b = float(x[2])
         c = float(x[3])
         d = float(x[4])
         x2 = [(a,b,c,d)]
         print('\n The Temp list is %s' %x2)
         x1 = [x[0]]
         #Ploting graph for temperature
         p1 = plt.plot(x[0],[e for(e,f,g,h) in x2],'rs')
         p2 = plt.plot(x[0],[f for(e,f,g,h) in x2],'bo')
         p3 = plt.plot(x[0],[g for(e,f,g,h) in x2],'g+')
         p4 = plt.plot(x[0],[h for(e,f,g,h) in x2],'c*')
    plt.xlabel('Time(sec)')
    plt.ylabel('Temp(C)')
    plt.title('Temperature Variance')
    plt.grid()
    plt.legend(loc = 'best')
    plt.legend((p1[0],p2[0],p3[0],p4[0]), ('Cur Temp','Min Temp','Avg Temp','Max Temp'))
    d = (12.0/(len(response['Messages']))) * 100
    plt.annotate('Data Retrieval rate is %s' %d, (0,0),(0,-100), xycoords='axes fraction', textcoords='offset points',va ='top')
    plt.gcf().autofmt_xdate()
    plt.show()
def button2_clicked():
    print('CtoF is clicked')
    sqs = boto3.client('sqs', region_name='us-west-2',
                   aws_access_key_id = 'AKIAJNQ4FNHFZP437GIQ',
                   aws_secret_access_key = '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')
    #printing queue url

    url = sqs.get_queue_url(QueueName='proj3_data_sqs')
    print(url['QueueUrl'])
    # Receiving messages from SQS queue

    response = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response1 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response2 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response['Messages'] = (response['Messages'] + response1['Messages'] + response2['Messages'])
    for i in range (0,30):
         message = response['Messages'][i]
         #Spliting string and taking timestamp value
         body = response['Messages'][i]['Body']
         print('\n The body content is %s' %body)
         x = body.split(",")
         print('\n The sliced string is %s' %x[0])
         a = ((9.0/5.0) * (float(x[1]))) + 32.0
         b = ((9.0/5.0) * (float(x[2]))) + 32.0
         c = ((9.0/5.0) * (float(x[3]))) + 32.0
         d = ((9.0/5.0) * (float(x[4]))) + 32.0
         x2 = [(a,b,c,d)]
         print('\n The Temp list is %s' %x2)
         x1 = [x[0]]
         #Ploting graph for temperature
         p1 = plt.plot(x[0],[e for(e,f,g,h) in x2],'rs')
         p2 = plt.plot(x[0],[f for(e,f,g,h) in x2],'bo')
         p3 = plt.plot(x[0],[g for(e,f,g,h) in x2],'g+')
         p4 = plt.plot(x[0],[h for(e,f,g,h) in x2],'c*')
    plt.xlabel('Time(sec)')
    plt.ylabel('Temp(F)')
    plt.title('Temperature Variance in Farenheit')
    plt.grid()
    plt.legend(loc = 'best')
    plt.legend((p1[0],p2[0],p3[0],p4[0]), ('Cur Temp','Min Temp','Avg Temp','Max Temp'))
    d = (12.0/(len(response['Messages']))) * 100
    plt.annotate('Data Retrieval rate is %s' %d, (0,0),(0,-100), xycoords='axes fraction', textcoords='offset points',va ='top')
    plt.gcf().autofmt_xdate()
    plt.show()
def button3_clicked():
    sqs = boto3.client('sqs', region_name='us-west-2',
                   aws_access_key_id = 'AKIAJNQ4FNHFZP437GIQ',
                   aws_secret_access_key = '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')
    #printing queue url

    url = sqs.get_queue_url(QueueName='proj3_data_sqs')
    print(url['QueueUrl'])
    # Receiving messages from SQS queue

    response = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response1 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response2 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response['Messages'] = (response['Messages'] + response1['Messages'] + response2['Messages'])
    #Checking length of messages for SQS check
    print(len(response['Messages']))
    if len(response['Messages']) == 30:
        t1.setText('Success')
    else:
        t1.setText(len(response['Messages']))
def button4_clicked():
    
    print('Execute Protocol Test button is clicked')
    mq = (mqttcalc.getMqttTime())
    coap = (asyncio.get_event_loop().run_until_complete(client_coap.coap_response()))
    web = ws_client.WebSocketResponse()
    amqp=amqp_send.AMQP_test()
           
           
    #Graph functionality with static values
    print("Getting MQTT DATA -----------------------------")
    rtt1 = mq  #MQTT
    print("Getting CoAP DATA -----------------------------")
    rtt2 = coap  #Websocket
    
    print("Getting WebSockets DATA -----------------------------")
    rtt3= web
    
    print("Getting AMQP DATA -----------------------------")
    rtt4 = amqp #AMQP
    
    #print(' The rtt is %s ms' %q.rtt)
    plt.xlabel('Protocols')
    plt.ylabel('Time Taken in seconds')
    p1 = plt.plot('MQTT',rtt1,'rs')
    p2 = plt.plot('CoAP',rtt2,'bo')
    p3 = plt.plot('Websocket',rtt3,'g+')
    p4 = plt.plot('AMQP',rtt4,'c*')
    plt.title('Performance analysis')
    plt.grid()
    plt.legend(loc = 'best')
    #plt.legend((p1[0],p2[0],p3[0]), ('MQTT','CoAP','WebSocket'))
    plt.legend((p1[0],p2[0],p3[0],p4[0]), ('MQTT','CoAP','WebSocket','AMQP'))
    plt.show()     


               
def b1_clicked():
    print('Pull Data Request button for Humidity is clicked')
    sqs = boto3.client('sqs', region_name='us-west-2',
                   aws_access_key_id = 'AKIAJNQ4FNHFZP437GIQ',
                   aws_secret_access_key = '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')
    #printing queue url

    url = sqs.get_queue_url(QueueName='proj3_data_sqs')
    print(url['QueueUrl'])
    # Receiving messages from SQS queue

    response = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response1 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response2 = sqs.receive_message(
               QueueUrl =  url['QueueUrl'],
               AttributeNames= [
                    'SentTimestamp'
               ],
               MaxNumberOfMessages = 10,
               MessageAttributeNames=[
                    'All'
               ],
               VisibilityTimeout = 0,
               WaitTimeSeconds = 0
               )
    response['Messages'] = (response['Messages'] + response1['Messages'] + response2['Messages'])

    for i in range (0,30):
         message = response['Messages'][i]
         print('Received message is  %s' %message)
         #Spliting string and taking timestamp value
         body = response['Messages'][i]['Body']
         print('\n The body content is %s' %body)
         x = body.split(",")
         print('\n The sliced string is %s' %x[0])
         a = float(x[5])
         b = float(x[6])
         c = float(x[7])
         d = float(x[8])
         x2 = [(a,b,c,d)]
         print('\n The Humidity list is %s' %x2)
         x1 = [x[0]]
         #Ploting graph for Humidity
         p1 = plt.plot(x[0],[e for(e,f,g,h) in x2],'rs')
         p2 = plt.plot(x[0],[f for(e,f,g,h) in x2],'bo')
         p3 = plt.plot(x[0],[g for(e,f,g,h) in x2],'g+')
         p4 = plt.plot(x[0],[h for(e,f,g,h) in x2],'c*')

    plt.xlabel('Time(sec)')
    plt.ylabel('Humidity')
    plt.title('Humidity Variance(%)')
    plt.grid()
    plt.legend(loc = 'best')
    plt.legend((p1[0],p2[0],p3[0],p4[0]), ('Cur Humidity','Min Humidity','Avg Humidity','Max Humidity'))
    d = (12.0/(len(response['Messages']))) * 100
    plt.annotate('Data Retrieval rate is %s' %d, (0,0),(0,-100), xycoords='axes fraction', textcoords='offset points',va ='top')
    plt.gcf().autofmt_xdate()
    plt.show()
def b2_clicked():
    #Quit Button
    print('Quit button is clicked')
    sys.exit(1)
def b3_clicked():
    print('Execute Protocol Test button for humidity is clicked')

def main():
     QT()
if __name__ == '__main__':
    main()