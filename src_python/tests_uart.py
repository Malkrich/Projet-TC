import serial
import time
import cv2

from uart import send_message_lamp

"""
NOTES :
Pin 14 = TX
Pin 15 = RX
"""


## initialisation serial
ser = serial.Serial('/dev/ttyS0',19200)

# programme
while True:
    data = ""
    current_data = ""
    while current_data != "x":
        current_data = ser.read().decode()
        data += current_data
        
    print(data)

## fin programme
ser.close()
