#include <modus.h>
#include <read_sensor.h>
#include <oled.h>
#include <sd_card.h>
#include <bluetooth.h>

unsigned long lastTime = 0;

void setup()
{
  Serial.begin(9600);
  // start_bluetooth();
  // start_sdCard();
  start_oled();

  // int n = 10;
  // float current_filter[n];
  // float voltage_filter[n];

  // Adjust Delay
  // if ((millis() - lastTime) > 1000)
  // {
  //   sendToApp(data);
  //   save_to_SD(data);
  //   Serial.println(data);
  //   lastTime = millis();
  // }
  for (int i = 0; i < 1000; i++)
  {
    float voltage = read_voltage();
    float current = read_current();
    float power = voltage * current;
    display_parameter(voltage, current, power);
    String data = String(voltage) + "V," + String(current) + "A," + String(power) + 'W';
    Serial.println(data);
    delay(250);
  }
  Serial.println("Finish");
}

void loop()
{
}