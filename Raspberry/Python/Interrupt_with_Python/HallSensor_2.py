#!/usr/bin/env python2.7
import multiprocessing as mp

import RPi.GPIO as GPIO
import time
import sys, os
from time import sleep

pipe_path = "/tmp/mypipe"
if not os.path.exists(pipe_path):
	os.mkfifo(pipe_path)
	
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

checkSecondLoop = 0
SpeedTime = 0
time_start = 0
rotation = 0
v = mp.Value('i', 12)

def f(x):
	return x*x

def my_callback(channel):
	global checkSecondLoop
	global SpeedTime
	global time_start
	global rotation
	if checkSecondLoop == 0:
		time_start = time.time()
		#print "1"
		checkSecondLoop = checkSecondLoop + 1;
	else:
		time_stop = time.time()
		SpeedTime = time_stop - time_start
		rotation = 0
		#print "2"
		checkSecondLoop = 0
		
def initGPIO():
	GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback)
	
def SpeedView():
	global checkSecondLoop
	global SpeedTime
	global time_start
	global rotation
	rotation = rotation + 1
	if rotation > 10:
		Speed = 0
		rotation = 10
	else:
		if SpeedTime:
			Speed = 1.0/SpeedTime*30
		else:
			Speed = 0.0
	print "\nSpeed = %f rpm" %Speed
	#print rotation
	os.system("echo %f > mypipe" %Speed )

if __name__ == '__main__':
	initGPIO()
	while True:
		try:
			SpeedView()
			sleep(1)
		except KeyboardInterrupt:
			sys.exit()
			GPIO.cleanup() # clean up GPIO on CTRL+C exit
			
	GPIO.cleanup() # clean up GPIO on normal exit
