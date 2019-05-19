Neopixel to control it with ESP8266  ESP-01 module and MQTT Raspberry as Broker: 

Control Commands

Each led stripe can set individual or group or all together.
For example all led together:
command ->„all“ „255,255,255,“  that means – 255 full brightness and the RGB signal: 			     (  255,255,255  means white | 255,0,0 = red; |  0,255,0 = green |   0,0,255 = blue

Example only led1 from the group 1full brightness and red:
	command ->  „Gruppe01/LED01“ „255, 0, 0,“

To using batteries for the ESP with WS2812 led I build a special voltage converter board.
