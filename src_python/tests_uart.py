import serial
import time
import cv2

"""
NOTES :
Pin 14 = TX
Pin 15 = RX
"""


## initialisation serial
ser = serial.Serial('/dev/ttyS0',19200)

# programme
commande = 
ser.write(str.encode(data))

## fin programme
ser.close()