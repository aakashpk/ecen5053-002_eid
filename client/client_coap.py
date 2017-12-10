import logging
import asyncio
import sqs_pull
from datetime import datetime

from aiocoap import *

logging.basicConfig(level=logging.INFO)

ipaddress="localhost"

async def coap_response():
    
    protocol = await Context.create_client_context()

    await asyncio.sleep(2)
    
    queue,length=sqs_pull.getSqsQueue()
    payload = str(queue).encode('utf-8')
    
    msg = Message(code=PUT, uri="coap://"+ipaddress+"/other/block", payload=payload)
    
    starttime=int(datetime.now().strftime("%f") )
    response = await protocol.request(msg).response
    endtime=int(datetime.now().strftime("%f"))
    #print('Result: %s\n%r'%(response.code, response.payload))
    print("Round Trip of ",length, "SQS messages")
    diff=endtime-starttime
    if(diff<0):
        diff=(1000000+diff)
    
    rtt=(diff)/1000
    print("Time Taken",rtt,"mS")
    return rtt

    
#print(asyncio.get_event_loop().run_until_complete(coap_response()))