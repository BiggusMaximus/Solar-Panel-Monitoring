import numpy as np
#from .timestamp import *
import pandas as pd
import serial
import time

data = []
ser = serial.Serial('COM3', 9600)  # ganti 'COM3' dengan nama port serial yang sesuai

def parsing_data():
    if ser.isOpen():
        data = ""
        while data != None:
            print('a')
            ser.write("Send Data".encode('utf-8'))
            data = ser.readline().strip().decode("utf-8")
            print(data)

def get_data():
    df = {
    'Voltage_generated': [], 
        'Current_generated': [], 
        'Power_generated': [],
        'Timestamp_generated' : [],
        'Voltage_used': [], 
        'Current_used': [], 
        'Power_used': [],
        'Timestamp_used' : [] 
    }

    voltage = np.random.rand()
    current = np.random.rand()
    power = np.random.rand()
    data.append(
        {
            'Voltage_generated': str(voltage), 
            'Current_generated': str(current), 
            'Power_generated': str(power),
            'Timestamp_generated' : get_time(),
            
            'Voltage_used': str(voltage), 
            'Current_used': str(current), 
            'Power_used': str(power),
            'Timestamp_used' : get_time()
        })
    
    df['Voltage_generated'].append(str(voltage))
    df['Current_generated'].append(str(voltage))
    df['Power_generated'].append(str(voltage))
    df['Timestamp_generated'].append(get_time())

    df['Voltage_used'].append(str(voltage))
    df['Current_used'].append(str(voltage))
    df['Power_used'].append(str(voltage))
    df['Timestamp_used'].append(get_time())

    df = pd.DataFrame(df)
    df.to_csv('data.csv', index=False)
    df.to_excel('data.xlsx', index=False)
    
    return data

while True:
    parsing_data()
