from tornado import escape
from tornado import gen
from tornado import httpclient
from tornado import httputil
from tornado import ioloop
from tornado import websocket
from datetime import datetime

import functools
import json
import time
import boto3


APPLICATION_JSON = 'application/json'

DEFAULT_CONNECT_TIMEOUT = 60
DEFAULT_REQUEST_TIMEOUT = 60

global starttime,endtime
 
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

        #self._ws_connection.write_message(escape.utf8(json.dumps(data)))
        
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
        print('\n Message received is %s' %msg)
        
        
        
        #pass

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
        print(msg)
        deadline = time.time() + 1
        ioloop.IOLoop().instance().add_timeout(
            deadline, functools.partial(self.send, str(int(time.time()))))

    def _on_connection_success(self):
        print('Connected!')
        #self.send(str(int(time.time())))
        #print('New Connection')
        sqs = boto3.client('sqs', region_name='us-west-2',
                  aws_access_key_id = 'AKIAJNQ4FNHFZP437GIQ',
                  aws_secret_access_key = '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')
        #printing queue url
        url = sqs.get_queue_url(QueueName='proj3_data_sqs')
        print(url['QueueUrl'])
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
        starttime=datetime.now().strftime("%f")
        print('\n The value of time is %s' %starttime)
        for i in range(0,30):
             msg = response['Messages'][i]
             #Spliting string and taking timestamp value
             body = response['Messages'][i]['Body']
             print('\n The body content is %s' %body)
             x = body.split(",")
             print('\n The sliced string is %s' %x[0])
             a = float(x[1])
             b = float(x[2])
             c = float(x[3])
             d = float(x[4])
             e = float(x[5])
             f = float(x[6])
             g = float(x[7])
             h = float(x[8])
             x6 = [(a,b,c,d)]
             print('\n The Temp list is %s' %x6)
             x1 = [x[0]]
             x2 = [x[1]]
             x3 = [x[2]]
             x4 = [x[3]]
             x5 = [x[4]]
             x7 = [x[5]]
             x8 = [x[6]]
             x9 = [x[7]]
             x10 = [x[8]]
             newmessage = '\0'
             msgreceived = '\0'
             Receivedmsg = ''
             #print('Sending back message: %s' % message)
             for x1,a,b,c,d,e,f,g,h in zip(x1,x2,x3,x4,x5,x7,x8,x9,x10):
                 newmessage+= "Time" + str(x1) + "\n" + "Cur Temp" + str(a) + "C\t" + "\n" + "Min Temp" + str(b) + "C\t" + "\n" + "Last Temp" + str(c) + "C\t" + "\n" + "Max Temp" + str(d) + "C\t" + "\n" + \
                              "Cur Hum" + str(e) + "%\t" + "\n" + "Min Hum" + str(f) + "%\t" + "\n" + "Last Hum" + str(g) + "%\t" + "\n" + "Max Hum" + str(h) + "%\t" 
                 self._ws_connection.write_message(newmessage)
        endtime=datetime.now().strftime("%f")
        print('\n The value of time is %s' %endtime)
        diff =  2 *(int(endtime) - int(starttime))
        if(diff < 0):
            diff = 100000 + diff
        rtt = diff/1000
        print('The rtt is %s ms' %rtt)

    def _on_connection_close(self):
        print('Connection closed!')

    def _on_connection_error(self, exception):
        print('Connection error: %s', exception)


def main():
    client = TestWebSocketClient()
    client.connect('ws://127.0.1.1:8888/ws')

    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        client.close()


if __name__ == '__main__':
    main()
