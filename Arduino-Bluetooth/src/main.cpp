#include <modus.h>
#include <read_sensor.h>
#include <oled.h>
#include <sd_card.h>
#include <bluetooth.h>

unsigned long lastTime = 0;

void setup()
{
  Serial.begin(9600);
  start_bluetooth();
  start_sdCard();
  start_oled();
}

void loop()
{
  int n = 10;
  float current_filter[n];
  float voltage_filter[n];

  for (int i = 0; i < n; i++)
  {
    current_filter[i] = read_current();
  }
  for (int i = 0; i < n; i++)
  {
    voltage_filter[i] = read_voltage();
  }
  float voltage = modus(voltage_filter, n);
  float current = modus(current_filter, n);
  float power = voltage * current;
  display_parameter(voltage, current, power);

  String data = String(voltage) + "V," + String(current) + "A," + String(power) + 'W';

  // Adjust Delay
  if ((millis() - lastTime) > 5000)
  {
    sendToApp(data);
    save_to_SD(data);
    lastTime = millis();
  }
}