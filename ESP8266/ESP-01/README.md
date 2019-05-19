<h1>Neopixel to control it with ESP8266  ESP-01 module and MQTT Raspberry as Broker:</h1> 


Video on YouTube --> <a href="https://youtu.be/n9nS4gmm7eU" target="_blank">
 <img src="https://user-images.githubusercontent.com/36192933/50377674-d0e70800-0621-11e9-9848-b41b02b2e1ac.png" alt="IMAGE ALT TEXT HERE" width="60" border="10" />
</a>
</br>

<a href="https://youtu.be/n9nS4gmm7eU" target="_blank"><img src="https://user-images.githubusercontent.com/36192933/57981045-035f2a80-7a33-11e9-9940-22850fbb1cdf.png" width="350"></a>
</br>

<h4>Control Commands</h4>

Each led stripe can set individual or group or all together.</br>
For example all led together:</br>
	command ->„all“ „255,255,255,“  </br>
	that means – 255 full brightness and the RGB signal:</br>
	(  255,255,255  means white | 255,0,0 = red; |  0,255,0 = green |   0,0,255 = blue</br>
</br>
Example only led1 from the group 1full brightness and red:</br></br>
	command ->  „Gruppe01/LED01“ „255, 0, 0,“</br>
</br>
<img src="https://user-images.githubusercontent.com/36192933/57981052-0c4ffc00-7a33-11e9-9db0-cd64a9ce38ed.jpg" width="350">
</br>
<b>To using batteries for the ESP with WS2812 led I build a special voltage converter board.</b>
</br>
<img src="https://user-images.githubusercontent.com/36192933/57981069-34d7f600-7a33-11e9-8be5-8278ddde3283.png" width="350">
