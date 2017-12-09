#!/usr/bin/env python3

# This file is part of the Python aiocoap library project.
#
# Copyright (c) 2012-2014 Maciej Wasilak <http://sixpinetrees.blogspot.com/>,
#               2013-2014 Christian Amsüss <c.amsuess@energyharvesting.at>
#
# aiocoap is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.

"""This is a usage example of aiocoap that demonstrates how to implement a
simple client. See the "Usage Examples" section in the aiocoap documentation
for some more information."""

import logging
import asyncio
import time
from datetime import datetime


from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()
	
    starttime=datetime.now().strftime("%f") #time.time()
    request = Message(code=GET, uri='coap://localhost/time')
    
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        endtime=datetime.now().strftime("%f")#time.time()
        print('Result: %s\n%r'%(response.code, response.payload))
        print(" Message Sent at:",starttime,"response at :",endtime) 
        print("difference",(int(endtime)-int(starttime)),"uS")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
