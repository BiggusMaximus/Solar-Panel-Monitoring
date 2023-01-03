#include <modus.h>
#include <read_sensor.h>
#include <oled.h>
#include <sd_card.h>
#include <bluetooth.h>
#include <lcd.h>

unsigned long interval=5000; // the time we need to wait
unsigned long previousMillis=0; // millis() returns an unsigned long.
float voltage, current;

void setup()
{
  Serial.begin(9600);
  start_lcd();
}

void loop()
{
  unsigned long currentMillis = millis();
  if ((unsigned long)(currentMillis - previousMillis) >= interval) {
    watt = read_voltage_avg_calibration() * read_current_avg();
    previousMillis = millis();
    voltage = read_voltage_avg_calibration();
    current = read_current_avg();
    lcd.clear();  

 }
  Serial.print(String(voltage) + "V   ||   ");
  Serial.print(String(current) + "A   ||   ");
  Serial.println(String(watt) + "W");
  lcd.setCursor(2,0);
  lcd.print(String(voltage) + "V");
  lcd.setCursor(9,0);
  lcd.print(current, 3);
  lcd.print("A");
  lcd.setCursor(2,1);
  lcd.print(String(watt) + "W");
  
}