from machine import I2C, Pin
import time
import ssd1306  

counter=0
value=1

checkSecondLoop = 0
SpeedTime = 0.0
time_start = 0.0
rotation = 0    

led = Pin(12, Pin.OUT)
button = Pin(13, Pin.IN)
i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

led.value(1)

def func(v):
    global value,counter
    global checkSecondLoop
    global SpeedTime
    global time_start
    global rotation

    if checkSecondLoop == 0:
        time_start = time.ticks_ms()
        print ("time_start " + str(time_start))
        checkSecondLoop = checkSecondLoop + 1;
    else:
        time_stop = time.ticks_ms()
        SpeedTime = time_stop - time_start
        rotation = 0
        print ("SpeedTime = " + str(SpeedTime))
        checkSecondLoop = 0
                
    counter+=1
    led.value(value)
    if(value == 0):
        value = 1
    else:
        value = 0
    display.fill(0) 
    display.text('Pi4IoT', 30, 0)  
    display.text('Counter: ' + str(counter), 5, 20) 
    display.text('Time: ' + str(SpeedTime) + 'ms', 5, 40)     
    print("IRQ ",counter)
    display.show()

def main():
    button.irq(trigger=Pin.IRQ_FALLING, handler=func)
    display.fill(0)
    display.text('Pi4IoT', 30, 0)
    display.text('Counter: ' + str(counter), 5, 20)
    display.text('Time: ' + str(SpeedTime) + 'ms', 5, 40) 
    display.show()

    while True:
        pass

        
if __name__ == "__main__":
    main()        


