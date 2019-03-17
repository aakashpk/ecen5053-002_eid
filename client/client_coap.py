import logging
import asyncio
import sqs_pull
from datetime import datetime
import time

from aiocoap import *

logging.basicConfig(level=logging.INFO)

ipaddress="192.168.43.185"

async def coap_response():
    
    protocol = await Context.create_client_context()

    await asyncio.sleep(2)
    
    queue,length=sqs_pull.getSqsQueue()
    payload = str(queue).encode('utf-8')
    
    msg = Message(code=PUT, uri="coap://"+ipaddress+"/other/block", payload=payload)
    
    starttime=time.time()
    response = await protocol.request(msg).response
    endtime=time.time()
    #print('Result: %s\n%r'%(response.code, response.payload))
    print("Round Trip of ",length, "SQS messages")
    rtt=endtime-starttime
    print("Start Time: ",starttime)
    print("End Time: ",endtime)
    print("Time Taken",rtt,"Seconds")
    return rtt

    
#print(asyncio.get_event_loop().run_until_complete(coap_response()))