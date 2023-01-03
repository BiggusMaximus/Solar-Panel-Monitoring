#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2); 

void start_lcd()
{
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(5,0);
  lcd.print("Start");
  lcd.clear();
  // delay(500);
}

void LCDdisplay_parameter(float v, float i, float w)
{
  lcd.setCursor(0, 0);
  lcd.print("V: " + String(v));
  lcd.setCursor(0, 1);
  lcd.print("I: " + String(i));
//   lcd.setCursor(0, 15);
//   lcd.print("W: " + String(w));
}