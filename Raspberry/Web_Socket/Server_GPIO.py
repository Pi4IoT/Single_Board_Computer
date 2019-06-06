#!/usr/bin/python

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

import datetime
import json

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(04, GPIO.IN)

class WSHandler(tornado.websocket.WebSocketHandler):

	def open(self):
		self.connected = True
		print 'new connection'
		self.write_message("LED = "+ str(GPIO.input(17)))
		self.write_message("Connection opend")
		self.timeout_loop()
		

	def on_message(self, message):
		print 'Incoming:', message
		if message == "led on":
			GPIO.output(17, True)
			self.write_message("LED = "+ str(GPIO.input(17)))
		elif message == "led off":
			GPIO.output(17, False)	
			self.write_message("LED = "+ str(GPIO.input(17)))
 
	def on_close(self):
		self.connected = False
		print 'connection closed'

	  
	def timeout_loop(self):
		if self.connected:	
			if GPIO.input(04) == 0:
				print "Button has been pressed"
				self.write_message("Button has been pressed")	
			tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=.1), self.timeout_loop)
			
application = tornado.web.Application([
	(r'/mycode', WSHandler),
])

if __name__ == "__main__":
	GPIO.output(17, False)	
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	print 'WebSocket Server start ..'
	tornado.ioloop.IOLoop.instance().start()
