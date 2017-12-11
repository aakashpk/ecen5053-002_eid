import sys
import socket
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import boto3
import itertools



class WSHandler(tornado.websocket.WebSocketHandler):
     def open(self):
         print('New Connection')
     def on_message(self, message):
         if(message != 'Done'):
              print('message received is %s' %message)
              self.write_message(message)
         if(message == 'Done'):
              print('Inside Done')
              print('message received is %s' %message)
              self.write_message('hello')
     def on_close(self):
         print('connection closed')
     def check_origin(self, origin):
         return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()


