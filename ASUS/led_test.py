import ASUS.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)

try:
        while 1:
                print "LED ON"
                GPIO.output(3,GPIO.HIGH)
                time.sleep(1)
                print "LED OFF"
                GPIO.output(3,GPIO.LOW)
                time.sleep(1)

finally: GPIO.cleanup()
