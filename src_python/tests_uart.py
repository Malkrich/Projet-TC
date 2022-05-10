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
#data = send_message_lamp(5)
#print("Sending : ",data)
#ser.write(str.encode(data))

while True:
    data = ser.read()
    print(data)

## fin programme
ser.close()
