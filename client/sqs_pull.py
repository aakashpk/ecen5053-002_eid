# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:46:19 2017

@author: Aakash
"""
import boto3


def getSqsQueue():
    print('Getting Data from Sqs Queue')
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
    
    #print(len(response))
    
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
    
    #print(len(response1))
    
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
    
    #print(len(response2))
    
    response = (response['Messages'] + response1['Messages'] + response2['Messages'])
    
    print(len(response))
    return response,len(response)

#print(getSqsQueue()[0]['Body'].split(","))


    