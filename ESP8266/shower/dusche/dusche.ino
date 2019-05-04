/*   Pi4IoT
 *   Wasser-Verbrauch für die Dusche
 *   Stromverbrauch:
 *   2.5mA in deepsleep mode
 *   25mA when running
 *   Version 1.0 30.04.2019 
 *   Board Adafruit Feather HUZZAH ESP8266
 *   www.youtube.com/pi4iot
*/
#include <ESP8266WiFi.h>
#include <GxEPD.h>
#include <GxGDEP015OC1/GxGDEP015OC1.h>    // 1.54" b/w
#include "dusche_3.h"
#include "dusche_4.h"

#include <Fonts/FreeMonoBold18pt7b.h>

#include <GxIO/GxIO_SPI/GxIO_SPI.h>
#include <GxIO/GxIO.h>
#define GPIO_Pin 5


GxIO_Class io(SPI, /*CS=D8*/3, /*DC=D3*/ 0, /*RST=D4*/ 2); 
GxEPD_Class display(io, /*RST=D4*/ 2, /*BUSY=D2*/ 4); 


unsigned long Startzeit = 0;
unsigned long Dauer = 0;
unsigned long Stopzeit = 0;
int sekunde = 0;
int minute = 0;
double liter = 0;
long wakeup = 0;


void setup()
{
  WiFi.mode(WIFI_OFF);
  WiFi.forceSleepBegin();
  pinMode(12, OUTPUT);
  digitalWrite(12, HIGH);
  attachInterrupt(digitalPinToInterrupt(GPIO_Pin), IntCallback, RISING);
  Startzeit = millis();
 }

void loop()
{  
  delay(500);
  if (wakeup > 2){
    display.init(115200); 
    pinMode(12, OUTPUT);
    digitalWrite(12, HIGH);
    display.setTextColor(GxEPD_BLACK);     // Schriftfarbe Schwarz
    display.setFont(&FreeMonoBold18pt7b);  // Schrift definieren
    delay(1000);
    display.drawExampleBitmap(gImage_dusche_3, 0, 0, 200, 200, GxEPD_WHITE);
    display.update();
    display.drawExampleBitmap(gImage_dusche_4, 0, 0, 200, 200, GxEPD_WHITE);
    display.update();
    delay(3000);   
    
    while(1){
      
        Dauer =  (millis() - Startzeit)/1000;
        sekunde = Dauer % 60;
        minute = Dauer / 60;
  
        display.fillRect(45, 105, 180, 170, GxEPD_WHITE); //Xpos,Ypos,box-w,box-h
        display.setCursor(45, 130);
        display.println(liter,1);
        display.setCursor(45, 163);

        if ((minute < 10)){
          display.print("0"); 
          display.print(minute);
          }
        else{
          display.print(minute);
        }
        display.print(":");
        if (sekunde < 10)
          display.print("0");
        display.print(sekunde);
  
        display.updateWindow(45, 105, 135, 65, false); 
        //if more the 5min no showered then go to sleep and restart
        if (((millis() - Stopzeit)/1000) > 300){
            //digitalWrite(10, LOW);
            ESP.deepSleep(30000000, RF_DISABLED); //sleep for 30sec
            delay(100);
        }
    }
  }

  ESP.deepSleep(15000000, WAKE_NO_RFCAL); //15sec

}

void IntCallback(){
 liter = liter + 0.0022;
 wakeup = wakeup + 1;
 Stopzeit = millis();
}

