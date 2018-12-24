"""
Pi4IoT    -> https://www.youtube.com/pi4iot
draw graphic like line, circle and fill rectangle on the ssd1306 display
"""

import ssd1306
from machine import I2C, Pin
import framebuf

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
fbuf = framebuf.FrameBuffer(bytearray(20 * 100 * 2), 120, 50, framebuf.MONO_VLSB)

def draw_line(display, x0, y0, x1, y1):
    deltax = x1 - x0
    deltay = y1 - y0
    error = -1.0
    deltaerr = abs(deltay / deltax)
    y = y0
    for x in range(int(x0), int(x1)-1):
        # plot(x,y)
        display.pixel(x, y, 1)
        # print(x, y)
        error = error + deltaerr
        if error >= 0.0:
            y = y + 1
            error = error - 1.0

def draw_circle(display, x0, y0, radius):
    x = radius
    y = 0
    err = 0

    while x >= y:
        display.pixel(x0 + x, y0 + y, 1)
        display.pixel(x0 + y, y0 + x, 1)
        display.pixel(x0 - y, y0 + x, 1)
        display.pixel(x0 - x, y0 + y, 1)
        display.pixel(x0 - x, y0 - y, 1)
        display.pixel(x0 - y, y0 - x, 1)
        display.pixel(x0 + y, y0 - x, 1)
        display.pixel(x0 + x, y0 - y, 1)
        y += 1
        err += 1 + 2*y
        if 2*(err-x) + 1 > 0:
            x -= 1
            err += 1 - 2*x        

display.fill(0)
draw_line(display,1,2,40,11)
draw_circle(display, 20, 40 , 20)

fbuf.text('Pi4IoT', 0, 0, 0xffff)
fbuf.hline(0, 10, 50, 0xffff)
fbuf.fill_rect(10, 20, 40, 30, 0xffff)    
display.framebuf.blit(fbuf, 60, 0)
display.show()
