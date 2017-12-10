import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

def coap_getResponse():
    
    protocol = await Context.create_client_context()

    #await asyncio.sleep(2)

    payload = b"The quick brown fox jumps over the lazy dog.\n" * 30
    #request = Message(code=PUT, payload=payload)
    # These direct assignments are an alternative to setting the URI like in
    # the GET example:
    #request.opt.uri_host = '192.168.43.185'
    #request.opt.uri_path = ("other", "block")
    
    msg = Message(code=PUT, uri="coap://192.168.43.185/other/block", payload=payload)
    
    response = await protocol.request(msg).response

    print('Result: %s\n%r'%(response.code, response.payload))
    
    
coap_getResponse()