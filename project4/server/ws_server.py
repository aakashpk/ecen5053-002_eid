import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
from tornado.options import define, options

import json
import socket

class WSHandler(tornado.websocket.WebSocketHandler):
    global unit
    def open(self):
        print ('c0nnected')
      
    def on_message(self, message):
        print (len(message))
        self.write_message(message)
        
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
    
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    myIP = socket.gethostbyname(socket.gethostname())
    print( '*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start() 

