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
  // start_oled();

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
  Serial.println("Start");
  // Serial.println(String(analog_avg()));
  for (int i = 0; i < 1000; i++)
  {
    // float voltage = read_voltage();
    // float current = read_current();
    // float power = voltage * current;
    // display_parameter(voltage, current, power);
    // String data = String(current);
    // Serial.println(data);
    // float voltage_filter[50];
    // float current_filter[50];
    // int n_modus = 50;

    // for (int i = 0; i < 50; i++)
    // {
    //   voltage_filter[i] = read_voltage_avg();
    // }
    // for (int i = 0; i < 50; i++)
    // {
    //   current_filter[i] = read_current();
    // }
    // float watt = (modus(voltage_filter, n_modus)) * (modus(current_filter, n_modus));

    //Serial.print(" Current: " + String(modus(current_filter, n_modus)));
    //Serial.println(" Watt: " + String(watt));
    
    Serial.println(String(read_voltage_avg_calibration()));
  }
  Serial.println("Finish");
}

void loop()
{
  // Serial.println(String(read_voltage_avg_calibration()));
  // delay(1000);
  // Serial.println(String(read_voltage_avg_calibration()));
  // delay(100);
}