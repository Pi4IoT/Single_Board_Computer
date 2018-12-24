from umqtt.simple import MQTTClient
from machine import I2C, Pin
import machine
import ubinascii
import ssd1306
 
# Setup a GPIO Pin for output
led = Pin(12, Pin.OUT)
button = Pin(13, Pin.IN)
pin = machine.Pin(2, machine.Pin.OUT) 
i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)


display.fill(0) 
display.text('Pi4IoT', 30, 0)  
display.text('LED: OFF', 30, 20)     
display.show()

# Modify below section as required
CONFIG = {
     # Configuration details of the MQTT broker
     "MQTT_BROKER": "192.168.0.42",
     "USER": "",
     "PASSWORD": "",
     "PORT": 1883,
     "TOPIC": b"test",
     # unique identifier of the chip
     "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}
 
# Method to act based on message received   
def onMessage(topic, msg):
    print("Topic: %s, Message: %s" % (topic, msg))
    display.fill(0)
    display.text('Pi4IoT', 30, 0)  
    if msg == b"on":
        pin.off()
        led.on()
        display.text('LED: ON', 30, 20)
    elif msg == b"off":
        pin.on()
        led.off()
        display.text('LED: OFF', 30, 20)
    display.show() 
      
def listen():
    #Create an instance of MQTTClient 
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
    # Attach call back handler to be called on receiving messages
    client.set_callback(onMessage)
    client.connect()
    client.publish(CONFIG['TOPIC'], "ESP8266 is Connected")
    client.publish(CONFIG['TOPIC'], "off")
    client.subscribe(CONFIG['TOPIC'])
    print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))
 
    try:
        while True:
            #msg = client.wait_msg()
            msg = (client.check_msg())
            if button.value() == 1:
                print("Button pressed")
                display.fill(0)
                display.text('Pi4IoT', 30, 0) 
                if led.value() == 1:
                    client.publish(CONFIG['TOPIC'], b"off")
                    display.text('LED: OFF', 30, 20) 
                else: 
                    client.publish(CONFIG['TOPIC'], b"on") 
                    display.text('LED: ON', 30, 20)
                display.show()  
                time.sleep_ms(500)
    finally:
        client.disconnect()  

listen()        
