
import boto3
import json
import datetime
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
from pylab import *
import pprint
pp = pprint.PrettyPrinter(indent=4)

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
            QueueUrl = url['QueueUrl'],
            AttributeNames =[
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
            QueueUrl = url['QueueUrl'],
            AttributeNames =[
                'SentTimestamp'
            ],
           MaxNumberOfMessages = 10,
           MessageAttributeNames=[
               'All'
           ],
           VisibilityTimeout = 0,
           WaitTimeSeconds = 0
          )

x3 = []
x4 = []
#plt.subplot(2,1,1)
#plt.subplot(2,1,2)
#print(response)
response['Messages']=(response['Messages']+response1['Messages']+response2['Messages'])
print(len(response['Messages']))

"""

for r in response['Messages']:    
    pp.pprint(response['Messages'])
"""
for i in range (0,30):
    message = response['Messages'][i]['Body']
    print('Received message is  %s' %message)
        
"""
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
         humidityList = [(x[5],x[6],x[7],x[8])]
         print('\n The humidity List is %s' %humidityList)
         x1 = [x[0]]
         #Ploting graph for temperature
         x3.append(x1)
         x4 += i *[x2]
         x5 = []
         x5 += i *[humidityList]
         for x1e,x2e in zip(x1,x2):
             plt.plot([x1e] * len(x2e), x2e)
         #for x1e, x5e in zip(x1,x5):
             #plt.plot([x1e] *len(x5e), x5e)

#for x3e,x4e in zip(x3,x4):
#    plt.plot(x3e *len(x4e), x4e)
plt.xlabel('Time(sec)')
plt.ylabel('Temp(C)')
plt.title('Temperature Variance')
plt.grid()
plt.gcf().autofmt_xdate()
plt.show()

for j in range (0,10):
        message1 = response1['Messages'][j]
        print('Received message is  %s' %message1)
        body1 = response1['Messages'][j]['Body']
        print('\n The body content is %s' %body1)
        x = body1.split(",")
        print('\n The sliced string is %s' %x[0])
        a = float(x[1])
        b = float(x[2])
        c = float(x[3])
        d = float(x[4])
        x2 = [(a,b,c,d)]
        print('\n The Temp list is %s' %x2)
        humidityList = [(x[5],x[6],x[7],x[8])]
        print('\n The humidity List is %s' %humidityList)
        x1 = [(x[0])]
         #Ploting graph for temperature
        x3.append(x1)
        x4 = []
        x4 += i *[x2]
        x5 = []
        x5 += i *[humidityList]
       # for x1e,x2e in zip(x1,x2):
        #     plt.plot([x1e] * len(x2e), x2e)
#plt.xlabel('Time(sec)')
#plt.ylabel('Temp(C)')
#plt.title('Temperature Variance')
#plt.grid()
#plt.gcf().autofmt_xdate()
#plt.show()

for k in range (0,10):
        message2 = response2['Messages'][k]
        print('Received message is  %s' %message2)
        body2 = response1['Messages'][j]['Body']
        print('\n The body content is %s' %body1)
        x = body2.split(",")
        print('\n The sliced string is %s' %x[0])
        a = float(x[1])
        b = float(x[2])
        c = float(x[3])
        d = float(x[4])
        x2 = [(a,b,c,d)]
        print('\n The Temp list is %s' %x2)
        humidityList = [(x[5],x[6],x[7],x[8])]
        print('\n The humidity List is %s' %humidityList)
        x1 = [(x[0])]
         #Ploting graph for temperature
        x3.append(x1)
        x4 = []
        x4 += i *[x2]
        x5 = []
        x5 += i *[humidityList]
        #for x1e,x2e in zip(x1,x2):
        #     plt.plot([x1e] * len(x2e), x2e)
#plt.xlabel('Time(sec)')
#plt.ylabel('Temp(C)')
#plt.title('Temperature Variance')
#plt.grid()
#plt.gcf().autofmt_xdate()
#plt.show()
"""