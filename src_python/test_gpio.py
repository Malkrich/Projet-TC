import cv2q
import RPi.GPIO as GPIO

SWITCH_LAMPE = 3

GPIO.setmode(GPIO.BOARD)

GPIO.setup(SWITCH_LAMPE,GPIO.OUT)

while(True):
    GPIO.output(SWITCH_LAMPE,0)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break



GPIO.cleanup()