## librairies standards
import numpy as np
import cv2
import RPi.GPIO as GPIO

## fonctions et class des fichiers externes
from detect_cible import main_contour
from class_form import form

## pin
SWITCH_LAMPE = 3

## Setup general
cap = cv2.VideoCapture(0)
f = form()
GPIO.setmode(GPIO.BOARD)

##setup pin
GPIO.setup(SWITCH_LAMPE,GPIO.OUT)

## lancement boucle infinie
while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    cnts = main_contour(frame)
    f.set_forme(0)
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)    
        cv2.drawContours(frame, [approx], -1, (0,255,0), 3)
        f.set_forme(len(approx))
        print(approx)
        f.display_info()
    
    GPIO.output(SWITCH_LAMPE,f.forme_exist())
    
    cv2.imshow('contours',frame)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

## fin programme
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()