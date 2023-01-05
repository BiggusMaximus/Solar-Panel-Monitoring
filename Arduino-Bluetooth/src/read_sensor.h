#include <Arduino.h>
#define R1 30000.0
#define R2 7500.0


float voltage_generated, current_generated, power_generated;
float voltage_used, current_used, power_used;

void analog_avg(int pin)
{
    float avg_analog = 0;
    for (int i = 0; i < 1000; i++)
    {
        avg_analog = avg_analog + analogRead(pin);
        delay(10);
    }
    avg_analog = avg_analog / 1000.0;
    Serial.println(avg_analog);
}

float read_voltage_avg(int pin)
{
    uint16_t avg_volt = 0;
    for (byte i = 0; i < 10; i++)
    {
        avg_volt = avg_volt + analogRead(pin);
    }
    avg_volt = avg_volt / 10;
    float volt = ((avg_volt * 5.0) / 1024.0) / (R2 / (R1 + R2));
    return volt;
}

float read_voltage_avg_calibration(int pin)
{
    uint16_t avg_volt = 0;
    for (byte i = 0; i < 10; i++)
    {
        avg_volt = avg_volt + analogRead(pin);
    }
    avg_volt = avg_volt / 10;
    float volt = 0.06449091372411075 + 0.024386004366555764 * avg_volt;
    return volt;
}

float read_voltage(int pin)
{
    uint16_t avg_volt = 0;
    avg_volt = avg_volt + analogRead(pin);
    float volt = ((avg_volt * 5.0) / 1024.0) / (R2 / (R1 + R2));
    return volt;
}

float read_current(int pin)
{
    uint16_t avg_curr = 0;
    avg_curr = avg_curr + analogRead(pin);
    float current = -24.944444156765247 + 0.04898098345792092 * avg_curr + 0.11;
    return current;
}

float read_current_avg(int pin)
{
    float avg_curr = 0;
    for (int i = 0; i < 1000; i++)
    {
        avg_curr = avg_curr + analogRead(pin);
    }
    avg_curr = avg_curr / 1000.0;
    float current = (2.5 - (avg_curr * (5.0 / 1024.0)) )/0.185 * avg_curr ;
    return current;
}

float read_current_avg_calibration(int pin)
{
    float avg_curr = 0;
    for (int i = 0; i < 1000; i++)
    {
        avg_curr = avg_curr + analogRead(pin);
    }
    avg_curr = avg_curr / 1000.0;
    float current = -24.944444156765247 + 0.04898098345792092 * avg_curr + 0.11;
    return current;
}

void read_all(){
    voltage_generated = read_voltage_avg_calibration(A7);
    voltage_used = read_voltage_avg_calibration(A6);
    current_generated = read_current_avg_calibration(A5);
    current_used = read_current_avg_calibration(A4);
    power_generated = voltage_generated * current_generated;
    power_used = voltage_used * current_used;

    Serial.println(
        String(voltage_generated) + "," +
        String(current_generated) + "," +
        String(power_generated) + "," +
        String(voltage_used) + "," +
        String(current_used) + "," +
        String(power_used) 
    );
}