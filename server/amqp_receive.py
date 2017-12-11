#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('10.201.18.143'))
#192.168.43.98
channel = connection.channel()


channel.queue_declare(queue='transmit')
channel.queue_declare(queue='receive')

def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    print("Recieved :",len(body))
    channel.basic_publish(exchange='',
                      routing_key='receive',
                      body=body)
    print("Sent back :",len(body))

channel.basic_consume(callback,
                      queue='transmit',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()