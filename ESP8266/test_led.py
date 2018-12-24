"""
Pi4IoT -> https://www.youtube.com/pi4iot
on off the blue LED on pin 2 
"""
import machine
import time
pin=machine.Pin(2, machine.Pin.OUT)

while True:
    pin.on()
    time.sleep(1)
    pin.off()
    time.sleep_ms(500)
