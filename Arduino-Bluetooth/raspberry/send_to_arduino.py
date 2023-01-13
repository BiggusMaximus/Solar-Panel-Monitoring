import serial
import time

serial_arduino = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    if serial_arduino.isOpen():
        serial_arduino.flushInput()
        val = serial_arduino.readline()
        while not '\\n' in str(val):
            time.sleep(.001)
            temp = serial_arduino.readline()
            if not not temp.decode():
                val = (val.decode()+temp.decode()).encode()
        val = val.decode().rstrip().split(',')

        voltage_generated = val[0]
        voltage_used = val[1]
        current_generated = val[2]
        current_used = val[3]
        power_used = val[4]
        power_generated = val[5]
        print(
            f"voltage generate : {val[0]}  \n current generate : {val[1]} \n piower generate : {val[2]} \n voltage used : {val[3]}  \n current used : {val[4]} \n piower used : {val[5]} \n")
