#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define SCREEN_ADDRESS 0x3C

Adafruit_SSD1306 display = Adafruit_SSD1306(128, 64, &Wire, -1);

void start_oled()
{
    if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS))
    {
        Serial.println(F("SSD1306 allocation failed"));
        for (;;)
            ; // Don't proceed, loop forever
    }
    else
    {
        Serial.println("OLED IS ABLE TO USE");
    }
    // text display tests
    display.setTextSize(2);
    display.setTextColor(SSD1306_WHITE);
    display.clearDisplay();
}

void display_parameter(float v, float i, float w)
{
    display.setCursor(0, 0);
    display.print("V: " + String(v));
    display.setCursor(0, 18);
    display.print("I: " + String(i));
    display.setCursor(0, 38);
    display.print("W: " + String(w));
    yield();
    display.display();
    display.clearDisplay();
}