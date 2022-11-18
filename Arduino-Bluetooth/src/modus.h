#include <Arduino.h>
float modus(float a[], int n)
{
    float maxValue = 0;
    float maxCount = 0;
    int i, j;

    for (i = 0; i < n; ++i)
    {
        float count = 0;

        for (j = 0; j < n; ++j)
        {
            if (a[j] == a[i])
                ++count;
        }

        if (count > maxCount)
        {
            maxCount = count;
            maxValue = a[i];
        }
    }
    return maxValue;
}