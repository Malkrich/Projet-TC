import serial
import time
import cv2

from uart import send_message_lamp,send_message_motor

"""
NOTES :
Pin 14 = TX
Pin 15 = RX
"""

action = 'write'

## initialisation serial
ser = serial.Serial('/dev/ttyS0',19200)

# programme
if action == 'read':
    print("reading data...")
    while True:
        data = ""
        current_data = ""
        while current_data != "x":
            current_data = ser.read().decode()
            data += current_data
            
        print(data)

#data = send_message_motor('front')
data = send_message_lamp(2)
if action == 'write':
    for c in data:
        print("Sending",c,"via UART")
        ser.write(str.encode(data))
    time.sleep(2)
    #data = send_message_motor('stop')
    data = send_message_lamp(-1)
    print("Sending",data,"via UART")
    ser.write(str.encode(data))

## fin programme
print("done")
ser.close()