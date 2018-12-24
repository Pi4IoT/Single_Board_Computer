import socket
import machine


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<h2>LED's on and off with Micropython</h2></center>
<h3>(ESP8266 HUZZAH Feather)</h3></center>
<form>
LED RED&nbsp;&nbsp;:
<button name="LED" value="ON_RED" type="submit">LED ON</button>
<button name="LED" value="OFF_RED" type="submit">LED OFF</button><br><br>
LED BLUE:
<button name="LED" value="ON_BLUE" type="submit">LED ON</button>
<button name="LED" value="OFF_BLUE" type="submit">LED OFF</button><br><br>
LED Extern:
<button name="LED" value="ON_EX" type="submit">LED ON</button>
<button name="LED" value="OFF_EX" type="submit">LED OFF</button>
</form>
</html>
"""

#Setup PINS
LED_RED = machine.Pin(0, machine.Pin.OUT)
LED_BLUE = machine.Pin(2, machine.Pin.OUT)
LED_EX = machine.Pin(12, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:

    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON_RED = request.find('/?LED=ON_RED')
    LEDOFF_RED = request.find('/?LED=OFF_RED')
    LEDON_BLUE = request.find('/?LED=ON_BLUE')
    LEDOFF_BLUE = request.find('/?LED=OFF_BLUE')
    LEDON_EX = request.find('/?LED=ON_EX')
    LEDOFF_EX = request.find('/?LED=OFF_EX')    

    if LEDON_RED == 6:
        print('TURN LED0 ON')
        LED_RED.off()
    if LEDOFF_RED == 6:
        print('TURN LED0 OFF')
        LED_RED.on()
    if LEDON_BLUE == 6:
        print('TURN LED2 ON')
        LED_BLUE.off()
    if LEDOFF_BLUE == 6:
        print('TURN LED2 OFF')
        LED_BLUE.on()
    if LEDON_EX == 6:
        print('TURN LED2 ON')
        LED_EX.on()
    if LEDOFF_EX == 6:
        print('TURN LED2 OFF')
        LED_EX.off()        
    response = html
    conn.send(response)
    conn.close()
