#!/usr/bin/env python
import pika
import sqs_pull
from datetime import datetime
import time

credentials = pika.PlainCredentials('project4', 'abcd')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.43.189',credentials=credentials))
#10.201.18.143
channel = connection.channel()

starttime=0
endtime=0
rtt=0

"""
def getRttVal():
    global endtime,rtt 
    endtime=int(datetime.now().strftime("%f"))
    #print("Received a new message: ")
    diff=endtime-starttime
    print(endtime)
    if(diff<0):
        diff=(1000000+diff)
    
    rtt=(diff)/1000
    print("AMQP Time Taken",rtt,"mS")
    return rtt

"""

channel.queue_declare(queue='transmit')
channel.queue_declare(queue='receive')

def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    global endtime,rtt 
    endtime=time.time()
    #print("Received a new message: ")
    rtt=endtime-starttime
    print("Start Time :",starttime)
    print("End Time :",endtime)
    print("AMQP Time Taken",rtt,"S")
    connection.close()
    return rtt
    
    

channel.basic_consume(callback,
                          queue='receive',
                          no_ack=True)

"""
queue,length=sqs_pull.getSqsQueue()
starttime=int(datetime.now().strftime("%f") )
channel.basic_publish(exchange='',
                          routing_key='transmit',
                          body=str(queue))
    
channel.start_consuming()


"""
def AMQP_test():
    global rtt,starttime
    
    queue,length=sqs_pull.getSqsQueue()
    
    starttime=time.time()
    print("date sent")
    channel.basic_publish(exchange='',
                          routing_key='transmit',
                          body=str(queue))
    channel.start_consuming()
    time.sleep(1)
    return rtt






