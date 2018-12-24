"""
Pi4IoT -> https://www.youtube.com/pi4iot
Get the CPU frequency and system version
"""
from machine import I2C, Pin
import time
import ssd1306  
import sys
import machine

   
i2c = I2C(-1, Pin(5), Pin(4))

display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.text('Pi4IoT', 30, 0)
display.text('CPU: ' + str(machine.freq()/1000000) + 'MHz', 1, 30)
display.text(sys.platform + " " + sys.version, 1, 45)

display.show()
