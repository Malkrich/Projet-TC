## librairies standards
import numpy as np
import cv2
import serial
import time

## fonctions et class des fichiers externes
from detect_cible import main_contour
from class_form import form
from uart import send_message_motor,send_message_lamp,read_data
from class_zone import zone_HG,zone_HD,zone_BG,zone_BD,zone_C


## Setup general
cap = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyS0',19200)
f = form()

## initialisation class zones
    # calcul des dimensions de l'image
ret, frame = cap.read()
h = len(frame)
w = len(frame[0])
l = (int)(w/3)
eps = (int)(h/3)
    # mise en place des differentes zones
haut_gauche = zone_HG(h,w,l,eps)
haut_droite = zone_HD(h,w,l,eps)
bas_gauche = zone_BG(h,w,l,eps)
bas_droite = zone_BD(h,w,l,eps)
centre = zone_C(h,w,l,eps)
liste_zone = [centre,haut_gauche,haut_droite,bas_gauche,bas_droite]

## lancement boucle infinie
while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    cnts = main_contour(frame)
    
    #distance = read_data(ser)
    #print(distance)
    
    f.clear_forme()
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)    
        cv2.drawContours(frame, [approx], -1, (0,255,0), 3)
        f.set_forme(approx)
        
        # affichage non nécessaire
        cX,cY = f.get_centre()
        cv2.circle(frame,(cX,cY),4,(0,255,0),-1)
        centre_str = str(cX) + ',' + str(cY)
        cv2.putText(frame, centre_str, (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        #f.display_info()
        
    #cX,cY = f.get_centre()
    
    # envoie de message si une forme existe
    #if f.forme_exist():
        #for z in liste_zone:
            #if z.in_zone(cX,cY):
                #data = send_message_lamp(z.get_zoneNb())
                #print(data)
                #ser.write(str.encode(data))
                #break

    cv2.imshow('contours',frame)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

## fin programme
cap.release()
cv2.destroyAllWindows()
ser.close()