#include <Arduino.h>
#define R1 30000.0
#define R2 7500.0
#define voltagePin A0
#define currentPin A1

float analog_avg(){
    uint16_t avg_analog = 0;
    for (byte i = 0; i < 10; i++)
    {
        avg_analog = avg_analog + analogRead(voltagePin);
    }
    avg_analog = avg_analog / 10;
    return avg_analog;
}

float read_voltage_avg()
{
    uint16_t avg_volt = 0;
    for (byte i = 0; i < 10; i++)
    {
        avg_volt = avg_volt + analogRead(voltagePin);
    }
    avg_volt = avg_volt / 10;
    float volt = ((avg_volt * 5.0) / 1024.0) / (R2 / (R1 + R2));
    return volt;
}

float read_voltage_avg_calibration(){
    uint16_t avg_volt = 0;
    for (byte i = 0; i < 10; i++)
    {
        avg_volt = avg_volt + analogRead(voltagePin);
    }
    avg_volt = avg_volt / 10;
    float volt = 0.06449091372411075 + 0.024386004366555764 * avg_volt;
    return volt;
}

float read_voltage()
{
    uint16_t avg_volt = 0;
    avg_volt = avg_volt + analogRead(voltagePin);
    float volt = ((avg_volt * 5.0) / 1024.0) / (R2 / (R1 + R2));
    return volt;
}

float read_current()
{
    uint16_t avg_curr = 0;
    avg_curr = avg_curr + analogRead(currentPin);
    float current = -7.516720252125317 + (0.01473662 * avg_curr);
    if (current < 0)
    {
        current = 0;
    }
    return current;
}

float read_current_avg()
{
    uint16_t avg_curr = 0;
    for (byte i = 0; i < 10; i++)
    {
        avg_curr = avg_curr + analogRead(currentPin);
    }
    avg_curr = avg_curr / 10;
    float current = -7.516720252125317 + (0.01473662 * avg_curr);
    // if (current < 0)
    // {
    //     current = 0;
    // }
    return current;
}
