#include <Arduino.h>
#include <SD.h>

File myFile;
int pinCS = 32;

void start_sdCard()
{
    pinMode(pinCS, OUTPUT);
    //-----SD Card Initialization-----
    if (SD.begin())
    {
        Serial.println("SD card is ready to use.");
    }
    else
    {
        Serial.println("SD card initialization failed.");
        return;
    }
}

void save_to_SD(String text)
{
    myFile = SD.open("data.txt", FILE_WRITE);
    if (myFile)
    {
        myFile.print(text);
    }
    else
    {
        Serial.println("error opening SolarPanel.txt");
    }
}
