#!/usr/bin/python

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

import datetime
import json

import smbus
import time
bus = smbus.SMBus(1)
address = 0x20
reset = 0
class WSHandler(tornado.websocket.WebSocketHandler):

	def open(self):
		self.connected = True
		statusLEDs =  bus.read_byte(address)
		print 'new connection', statusLEDs
		bus.write_byte(address, (statusLEDs & 0b11011111))
		self.timeout_loop()
		self.write_message("Welcome! The LEDs Value is = " + str(statusLEDs))
	def on_message(self, message):
		print 'Incoming:', message
		
		if message == "LED1 on":
			statusLEDs =  bus.read_byte(address)
			bus.write_byte(address, (statusLEDs & 0b11111110))
			time.sleep(1)
		if message == "LED1 off":
			statusLEDs =  bus.read_byte(address)
			if (statusLEDs & 0b00000001):
				print 'is already off'
				self.write_message("LED 1 is already off")
			else:
				bus.write_byte(address, (statusLEDs + 0b00000001))
				time.sleep(1)		

		if message == "LED2 on":
			statusLEDs =  bus.read_byte(address)
			bus.write_byte(address, (statusLEDs & 0b11111101))
			time.sleep(1)
		if message == "LED2 off":
			statusLEDs =  bus.read_byte(address)
			if (statusLEDs & 0b00000010):
				print 'is already off'
				self.write_message("LED 2 is already off")
			else:
				bus.write_byte(address, (statusLEDs + 0b00000010))
				time.sleep(1)	
						
		if message == "LED3 on":
			statusLEDs =  bus.read_byte(address)
			bus.write_byte(address, (statusLEDs & 0b11111011))
			time.sleep(1)
		if message == "LED3 off":
			statusLEDs =  bus.read_byte(address)
			if (statusLEDs & 0b00000100):
				print 'is already off'
				self.write_message("LED 3 is already off")
			else:
				bus.write_byte(address, (statusLEDs + 0b00000100))
				time.sleep(1)	
				
		if message == "LED4 on":
			statusLEDs =  bus.read_byte(address)
			bus.write_byte(address, (statusLEDs & 0b11110111))
			time.sleep(1)
		if message == "LED4 off":
			statusLEDs =  bus.read_byte(address)
			if (statusLEDs & 0b00001000):
				print 'is already off'
				self.write_message("LED 4 is already off")
			else:
				bus.write_byte(address, (statusLEDs + 0b00001000))
				time.sleep(1)
		statusLEDs =  bus.read_byte(address)		
		self.write_message("Your message:" + message + " ../The Port Value is = " + str(statusLEDs))	
 
	def on_close(self):
		self.connected = False
		statusLEDs =  bus.read_byte(address)
		bus.write_byte(address, (statusLEDs | 0b11110000))
		print 'connection closed'

	  
	def timeout_loop(self):
		global reset
		if self.connected:
			statusLEDs =  bus.read_byte(address)
			bus.write_byte(address, (statusLEDs & 0b11001111))
			pin_in =  ~bus.read_byte(address)
			if pin_in & 0b10000000:
				self.write_message("Taster 1 was pressed"+ " ../The Port Value is = " + str(statusLEDs))
				reset = 3
				time.sleep(0.1)
			elif pin_in & 0b01000000:
				self.write_message("Taster 2 was pressed"+ " ../The Port Value is = " + str(statusLEDs))
				reset = 3
				time.sleep(0.1)
			bus.write_byte(address, (statusLEDs | 0b11000000))
			if reset > 1:
				reset = reset - 1
				if reset == 1:	
					self.write_message("..The Port Value is = " + str(statusLEDs))
					print "reset taster"
								
			tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=.1), self.timeout_loop)
			
 
 
application = tornado.web.Application([
	(r'/mycode', WSHandler),
])

if __name__ == "__main__":
	bus.write_byte(address, 0xff)
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	print 'WebSocket Server start ..'
	tornado.ioloop.IOLoop.instance().start()
