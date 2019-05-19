/*
 * 19.05.2019 Pi4IoT
 * Board - Generic ESP8266 Module 
 * client as Subscriber
 * Arduino IDE Vers. 1.8.2
 */
 
#include <Adafruit_NeoPixel.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//your Info for the WLAN Router.....
const char* SSID = "Your SSID";        //WLAN Router
const char* PSK = "Your Password";     //WLAN Router
const char* MQTT_BROKER = "Your IP Number ";  //Raspberry Pi

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

int red = 0;
int green = 0;
int blue = 0;

#define PIN            2

#define NUMPIXELS      8
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN,NEO_GRB + NEO_KHZ800);
int fac = 0;

void setup() {
  Serial.begin(115200);
  pixels.begin();

  for(int i = 0; i < 10; i++){
      pixels.setPixelColor(0, pixels.Color(0,0,0));   pixels.show();  delay(200);
      pixels.setPixelColor(0, pixels.Color(10,0,0));  pixels.show();  delay(100);    
     }
  setup_wifi();
  client.setServer(MQTT_BROKER, 1883);
  client.setCallback(callback);
  
  for(int i = 0; i < 2; i++){
      pixels.setPixelColor(0, pixels.Color(0,0,0));  pixels.show();  delay(200);
      pixels.setPixelColor(0, pixels.Color(0,0,10)); pixels.show();  delay(100);    
     }
  pixels.setPixelColor(0, pixels.Color(0,10,0)); pixels.show();  delay(1000);
  pixels.setPixelColor(0, pixels.Color(0,0,0));
  pixels.setPixelColor(1, pixels.Color(0,0,0));
  pixels.setPixelColor(2, pixels.Color(0,0,0));
  pixels.setPixelColor(3, pixels.Color(0,0,0));
  pixels.setPixelColor(4, pixels.Color(0,0,0));
  pixels.setPixelColor(5, pixels.Color(0,0,0));
  pixels.setPixelColor(6, pixels.Color(0,0,0));
  pixels.setPixelColor(7, pixels.Color(0,0,0));
  pixels.show();
}

void setup_wifi() {
    delay(10);
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(SSID);
 
    WiFi.begin(SSID, PSK);
 
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
 
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
    char msg[length+1];
    for (int i = 0; i < length; i++) {
        msg[i] = (char)payload[i];
    }
    msg[length] = '\0';

//**********************************  reaction for which topic  *******************************************  
 if(strcmp(topic,"all")==0 or strcmp(topic,"Gruppe01")==0 or strcmp(topic,"Gruppe01/LED01")==0){
    red = (split(msg, ',',0).toInt());
    green = (split(msg, ',',1).toInt());
    blue =   (split(msg, ',',2).toInt());

        pixels.setPixelColor(0, pixels.Color(red, green, blue));
        pixels.setPixelColor(1, pixels.Color(red, green, blue));
        pixels.setPixelColor(2, pixels.Color(red, green, blue));
        pixels.setPixelColor(3, pixels.Color(red, green, blue));
        pixels.setPixelColor(4, pixels.Color(red, green, blue));
        pixels.setPixelColor(5, pixels.Color(red, green, blue));
        pixels.setPixelColor(6, pixels.Color(red, green, blue));
        pixels.setPixelColor(7, pixels.Color(red, green, blue));
        pixels.show();
 }
}
 
void reconnect() {
    while (!client.connected()) {
        Serial.println("Reconnecting MQTT...");
        
//********************************** unique name for each ESP *********************************************        
        if (!client.connect("LED_01_01")) //!!!!unique name for each ESP
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" retrying in 5 seconds");
            delay(5000);
        }
    }
    client.subscribe("#");
    Serial.println("MQTT Connected...");
}

String split(String s, char parser, int index) {
  String rs="";
  int parserIndex = index;
  int parserCnt=0;
  int rFromIndex=0, rToIndex=-1;
  while (index >= parserCnt) {
    rFromIndex = rToIndex+1;
    rToIndex = s.indexOf(parser,rFromIndex);
    if (index == parserCnt) {
      if (rToIndex == 0 || rToIndex == -1) return "";
      return s.substring(rFromIndex,rToIndex);
    } else parserCnt++;
  }
  return rs;
}

void loop() {
  if (!client.connected()) {
      reconnect();
    }
  client.loop();
}
