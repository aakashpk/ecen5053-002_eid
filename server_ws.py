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
        print ('new connection')
        self.write_message('connected')   

      
    def on_message(self, message):
        print ('Message Received  %s' % message)
        self.write_message(message)
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html') 

class StaticFileHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('main.js')
    
application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r"/", IndexHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path':  './'}),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    myIP = socket.gethostbyname(socket.gethostname())
    print( '*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start() 

