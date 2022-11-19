#include <Arduino.h>
#include <SD.h>
#include <SPI.h>
File myFile;
int pinCS = 32;

void start_sdCard()
{
    pinMode(pinCS, OUTPUT);
    //-----SD Card Initialization-----
    if (SD.begin(32))
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
    if (SD.exists("data.txt"))
    {
        myFile = SD.open("data.txt", FILE_WRITE);
        if (myFile)
        {
            myFile.println(text);
            myFile.close();
        }
        else
        {
            SD.remove("data.txt");
            Serial.println("error opening SolarPanel.txt");
        }
    }
    else
    {
        Serial.println("File didnt found");
    }
}

void read_SD(String text)
{
    if (SD.exists("data.txt"))
    {
        myFile = SD.open("data.txt");
        if (myFile)
        {
            Serial.println("data.txt:");

            // read from the file until there's nothing else in it:
            while (myFile.available())
            {
                Serial.write(myFile.read());
            }
            // close the file:
            myFile.close();
        }
        else
        {
            // if the file didn't open, print an error:
            Serial.println("error opening test.txt");
        }
    }

    else
    {
        Serial.println("File didnt found");
    }
}