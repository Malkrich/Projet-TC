## librairies standards
import numpy as np
import cv2
import serial
import time

## fonctions et class des fichiers externes
from class_form import form
from class_zone import zone_HG,zone_HD,zone_BG,zone_BD,zone_C
from class_robot import robot

from detect_cible import main_contour
from uart import send_message_motor,send_message_lamp,read_data
from f_pilote_automatique import premier_tour


## Setup general
cap = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyS0',19200)
f = form()
rob = robot()

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

## Initialisation variables pilote automatique
nb_cible = 4
nb_cible_touche= 0
coord_init = [1,1]
coord_actuelle = [1,1]
orientation_actuelle = 0
distance_decalage = 2
compteur_exploration = 1
taille_map=10
distance_min_mvmt=1

## lancement boucle infinie
while(True):
    #distance = read_data(ser)
    #print(distance)
    
    # pilotage automatique
    distance = 50
    rob.maj_distance(distance)

    # Capture frame by frame
    ret, frame = cap.read()
    
    cnts = main_contour(frame)
    
    f.clear_forme()
    rob.maj_cible('')
    
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
        
    cX,cY = f.get_centre()
    
    # envoie de message si une forme existe
    if f.forme_exist():
        for z in liste_zone:
            if z.in_zone(cX,cY):
                rob.maj_cible(send_message_lamp(z.get_zoneNb()))
                break

    # envoie info
    rob.make_decision()
    code_uart = rob.get_message()
    print(code_uart)
    cv2.imshow('contours',frame)
    ser.write(str.encode(code_uart))
    #rob.tempo()
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

## fin programme
code_uart = send_message_motor('stop')
ser.write(str.encode(code_uart))
cap.release()
cv2.destroyAllWindows()
ser.close()