#include "Wire.h"
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
#include <Sensirion.h>

Adafruit_PCD8544 display = Adafruit_PCD8544( 13, 11, 16, 15, 14);
// SHT75 on PIN 19 + 20
const uint8_t dataPin  =  19;
const uint8_t clockPin =  18;

float temperature;
float humidity;
float dewpoint;

Sensirion tempSensor = Sensirion(dataPin, clockPin);

void setup()
{ 
  display.begin();
  display.setContrast(65);
  display.setRotation(90);
  display.setTextSize(1);
  display.setTextColor(BLACK);
  display.clearDisplay();
   
   delay(4000);
   display.display();

} 

void loop ()    
{
   printSHT75();
}
void printSHT75(){
  tempSensor.measure(&temperature, &humidity, &dewpoint);
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




