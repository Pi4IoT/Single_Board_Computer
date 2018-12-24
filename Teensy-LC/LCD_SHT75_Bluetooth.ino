#include "Wire.h"
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
#include <Sensirion.h>

Adafruit_PCD8544 display = Adafruit_PCD8544( 13, 11, 16, 15, 14);

const int led = 5;
String incoming ;

const uint8_t dataPin  =  19;
const uint8_t clockPin =  18;

float temperature;
float humidity;
float dewpoint;

Sensirion tempSensor = Sensirion(dataPin, clockPin);

void setup()
{ 
  Serial1.begin(115200); 

  display.begin();
  display.setContrast(65);
  display.setRotation(90);
  display.setTextSize(1);
  display.setTextColor(BLACK);
  display.clearDisplay();
   
   display.println("Bluetooth");
   display.println("---------");
   display.println("is ready");
   delay(4000);
   display.display();

   pinMode(led, OUTPUT);
   digitalWrite(led, LOW);
} 

void loop ()    
{
   printDate();
   printSHT75();
}
void printSHT75(){
  tempSensor.measure(&temperature, &humidity, &dewpoint);
  Serial1.print("Temperature: ");
  Serial1.print(temperature);
  Serial1.println(" C");
  Serial1.print("Humidity: ");
  Serial1.print(humidity);
  Serial1.println(" %");
  Serial1.print("Dewpoint: ");
  Serial1.print(dewpoint);
  Serial1.println(" C");
  Serial1.println("----------------");

  display.clearDisplay();
  display.setCursor(0,0);
  display.println("---Pi4IoT---");
  display.println("------------");
  display.print(" T: ");
  display.print(temperature);
  display.println(" C");
  display.print(" H: ");
  display.print(humidity);
  display.println(" %");
  display.println("");
  display.print("Dew: ");
  display.print(dewpoint);
  display.println(" C");
  display.display();
  delay(1000);  
  
}
void printDate(){   
     if(Serial1.available())
       {
        incoming = Serial1.readStringUntil('\n');
        if(incoming == "on"){
           digitalWrite(led, HIGH);
           Serial1.println("okay..");
          }
        if(incoming == "off"){
           digitalWrite(led, LOW);
           Serial1.println("okay...");   
          }
        display.clearDisplay();
        display.setCursor(0,0);
        Serial1.println(incoming);
        display.println(incoming);
        display.display();
       }
    delay(100);
 }




