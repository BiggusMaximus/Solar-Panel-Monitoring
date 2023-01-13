import numpy as np
from .timestamp import *
import pandas as pd
import serial
import time

data = []
serial_arduino = serial.Serial('/dev/ttyUSB0', 9600)


def parsing_data():
    if serial_arduino.isOpen():
        serial_arduino.flushInput()
        val = serial_arduino.readline()
        time.sleep(.001)
        temp = serial_arduino.readline()
        if not not temp.decode():
            val = (val.decode()+temp.decode()).encode()
        val = val.decode().rstrip().split(',')
        print(val)
        print("data func")
        return val


def get_data():
    df = {
        'Voltage_generated': [],
        'Current_generated': [],
        'Power_generated': [],
        'Timestamp_generated': [],
        'Voltage_used': [],
        'Current_used': [],
        'Power_used': [],
        'Timestamp_used': []
    }
    print("get_data")
    val = parsing_data()
    voltage_generated = val[0]
    voltage_used = val[1]
    current_generated = val[2]
    current_used = val[3]
    power_used = val[4]
    power_generated = val[5]

    data.append(
        {
            'Voltage_generated': str(voltage_generated),
            'Current_generated': str(current_generated),
            'Power_generated': str(power_generated),
            'Timestamp_generated': get_time(),

            'Voltage_used': str(voltage_used),
            'Current_used': str(current_used),
            'Power_used': str(power_used),
            'Timestamp_used': get_time()
        })

    df['Voltage_generated'].append(str(voltage_generated))
    df['Current_generated'].append(str(current_generated))
    df['Power_generated'].append(str(power_generated))
    df['Timestamp_generated'].append(get_time())

    df['Voltage_used'].append(str(voltage_used))
    df['Current_used'].append(str(current_used))
    df['Power_used'].append(str(power_used))
    df['Timestamp_used'].append(get_time())

    df = pd.DataFrame(df)
    df.to_csv('data.csv', index=False)
    df.to_excel('data.xlsx', index=False)

    return data


while True:
    parsing_data()
