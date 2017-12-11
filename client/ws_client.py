"""Simple Web socket client implementation using Tornado framework.
"""

from tornado import escape
from tornado import gen
from tornado import httpclient
from tornado import httputil
from tornado import ioloop
from tornado import websocket

import functools
import json
import time
import boto3
import sqs_pull

APPLICATION_JSON = 'application/json'

DEFAULT_CONNECT_TIMEOUT = 60
DEFAULT_REQUEST_TIMEOUT = 60

starttime=0
endtime=0
rtt=0

class WebSocketClient():
    """Base for web socket clients.
    """
 
    def __init__(self, *, connect_timeout=DEFAULT_CONNECT_TIMEOUT,
                 request_timeout=DEFAULT_REQUEST_TIMEOUT):

        self.connect_timeout = connect_timeout
        self.request_timeout = request_timeout

    def connect(self, url):
        """Connect to the server.
        :param str url: server URL.
        """

        headers = httputil.HTTPHeaders({'Content-Type': APPLICATION_JSON})
        request = httpclient.HTTPRequest(url=url,
                                         connect_timeout=self.connect_timeout,
                                         request_timeout=self.request_timeout,
                                         headers=headers)
        ws_conn = websocket.WebSocketClientConnection(ioloop.IOLoop.current(),
                                                      request)
        ws_conn.connect_future.add_done_callback(self._connect_callback)

    def send(self, data):
        """Send message to the server
        :param str data: message.
        """
        if not self._ws_connection:
            raise RuntimeError('Web socket connection is closed.')

        self._ws_connection.write_message(escape.utf8(json.dumps(data)))

    def close(self):
        """Close connection.
        """

        if not self._ws_connection:
            raise RuntimeError('Web socket connection is already closed.')

        self._ws_connection.close()

    def _connect_callback(self, future):
        if future.exception() is None:
            self._ws_connection = future.result()
            self._on_connection_success()
            self._read_messages()
        else:
            self._on_connection_error(future.exception())

    @gen.coroutine
    def _read_messages(self):
        while True:
            msg = yield self._ws_connection.read_message()
            if msg is None:
                self._on_connection_close()
                break

            self._on_message(msg)

    def _on_message(self, msg):
        """This is called when new message is available from the server.
        :param str msg: server message.
        """

        pass

    def _on_connection_success(self):
        """This is called on successful connection ot the server.
        """

        pass

    def _on_connection_close(self):
        """This is called when server closed the connection.
        """
        pass

    def _on_connection_error(self, exception):
        """This is called in case if connection to the server could
        not established.
        """

        pass



class TestWebSocketClient(WebSocketClient):

    def _on_message(self, msg):
        global starttime,endtime,rtt
        endtime=time.time()
        print("End time: ",endtime)
        rtt=endtime-starttime
        print("time taken",rtt)
        print("Got back",len(msg))
        client.close()
        ioloop.IOLoop.instance().stop()
        return rtt
        
    def _on_connection_success(self):
        #print('Connected!')
        global starttime
        queue,length=sqs_pull.getSqsQueue()
        starttime=time.time()
        print("Start time",starttime)
        self.send(str(queue))
        #self.send(str(int(time.time())))

    def _on_connection_close(self):
        print('Connection closed!')

    def _on_connection_error(self, exception):
        print('Connection error: %s', exception)


def WebSocketResponse():
    global rtt,client
    client = TestWebSocketClient()
    #echo.websocket.org
    client.connect('ws://192.168.43.185:8080/ws')
       
    ioloop.IOLoop.instance().start()
    return rtt

#WebSocketResponse()
