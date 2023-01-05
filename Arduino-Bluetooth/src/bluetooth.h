#include <Arduino.h>
#include <SoftwareSerial.h>
SoftwareSerial bluetooth(12, 11);
bool showColumn = true;

void start_bluetooth()
{
    bluetooth.begin(9600);
    // Serial.println("Bluetooth is able to use");
}

void sendToApp(String text)
{
    if (showColumn)
    {
        bluetooth.println("current,voltage,power");
        showColumn = false;
    }
    Serial.println("text");
    bluetooth.println(text);
    Serial.println("end");
    Serial.println(text);

}