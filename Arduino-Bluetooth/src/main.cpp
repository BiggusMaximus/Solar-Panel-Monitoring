#include <modus.h>
#include <read_sensor.h>
#include <oled.h>
#include <sd_card.h>
#include <bluetooth.h>
#include <lcd.h>
#include "serial.h"

void setup()
{
  Serial.begin(9600);
  start_bluetooth();
  // start_lcd();
}

void loop()
{
  read_all();
  delay(300);

  // if(Serial.available() > 0)
  // {
  //   char c=Serial.read();
  //   if(c=='A')
  //   {
  //      delay(1000);
  //   Serial.print("OK");
  //   }
  // }
}