## librairies standards
import numpy as np
import cv2

## fonctions et class des fichiers externes
from detect_cible import main_contour
from class_form import form
from uart import send_message_motor,send_message_lamp


## Setup general
cap = cv2.VideoCapture(0)
f = form()

## lancement boucle infinie
while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    cnts = main_contour(frame)
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)    
        cv2.drawContours(frame, [approx], -1, (0,255,0), 3)
        f.set_forme(approx)
        
        # affichage non nécessaire
        cX,cY = f.get_centre()
        cv2.circle(frame,(cX,cY),4,(0,255,0),-1)
        f.display_info()
        
    cv2.imshow('contours',frame)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

## fin programme
cap.release()
cv2.destroyAllWindows()