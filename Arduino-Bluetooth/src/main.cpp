#include <modus.h>
#include <read_sensor.h>
#include <oled.h>
#include <sd_card.h>
#include <bluetooth.h>
#include <lcd.h>

unsigned long lastTime = 0;

void setup()
{
  Serial.begin(9600);
  Serial.println("Start");
  analog_avg();
  Serial.println("end");
  // start_lcd();
}

void loop()
{
  // float watt = read_voltage_avg_calibration() * read_current_avg();
  // Serial.print(String(read_voltage_avg_calibration()) + "V   ||   ");
  // Serial.print(String(read_current_avg()) + "A   ||   ");
  // Serial.println(String(watt) + "W");

  // lcd.setCursor(2,0);
  // lcd.print(String(read_voltage_avg_calibration()) + "V");
  // lcd.setCursor(9,0);
  // lcd.print(String(read_current_avg()) + "A");
  // lcd.setCursor(2,1);
  // lcd.print(String(watt) + "W");
  // delay(500);
  // lcd.clear();
}