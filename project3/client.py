#!/usr/bin/python
# Author : Hari Shreenivash
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import sys
import json
import datetime
#import Adafruit_DHT
import boto3
import matplotlib.pyplot as plt
from PyQt5 import QtGui, QtCore , QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqs_pull
#QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout

def QT():
    global t1
    ##### Creating an object for the application ################
    app = QApplication(sys.argv)
    ####### Declaring Tabs ########################################
    tabs = QtWidgets.QTabWidget()
    tab1 = QtWidgets.QWidget()
    tab2 = QtWidgets.QWidget()
    tabs.resize (1700, 1700)
    ####### Setting a Window Title ################################
    tabs.setWindowTitle("Temperature and Humidity")
    ######  Creating Vertical Box layout for tab1  ################
    vBoxlayout = QtWidgets.QVBoxLayout()
    tab1.setLayout(vBoxlayout)
    ####### Creating Vertical Box Layout for tab2  ################
    vBoxlayout = QtWidgets.QVBoxLayout()
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
    ################### Creating buttons for tab2####################
    b1 = QPushButton(tab2)
    b2 = QPushButton(tab2)
    ################## Names of buttons in tab1 ###########################
    button1.setText("Data Request")
    button1.move(300,100)
    button2.setText("CtoF")
    button2.move(300,300)
    button3.setText("SQS  Check")
    button3.move(100,100)
    ################### Button 2 #################################
    b1.setText("Data Request")
    b1.move(300,100)
    b2.setText("Quit")
    b2.move(300,300)
    ############## Defining actions for buttons ##################
    button1.clicked.connect(button1_clicked)
    button2.clicked.connect(button2_clicked)
    button3.clicked.connect(button3_clicked)
    b1.clicked.connect(b1_clicked)
    b2.clicked.connect(b2_clicked)
    tabs.show()
    sys.exit(app.exec_())

def button1_clicked():
    
    response['Messages']=sqs_pull.getSqsQueue()
    
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

    #TODO: remove secret key from code and pick from config files.
def button2_clicked():
    print('CtoF is clicked')
    sqs = boto3.client('sqs', region_name='us-west-2',
                   aws_access_key_id = 'access-key',
                   aws_secret_access_key = 'secret-key')
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
def main():
     QT()
if __name__ == '__main__':
    main()
