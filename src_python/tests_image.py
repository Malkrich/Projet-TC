import cv2
import numpy as np

from class_zone import zone_HG,zone_HD,zone_BG,zone_BD,zone_C

cap = cv2.VideoCapture(0)

# calcul hauteur, largeur
ret, frame = cap.read()
h = len(frame)
w = len(frame[0])
l = (int)(w/3)
eps = (int)(h/3)

## class zones
haut_gauche = zone_HG(h,w,l,eps)
haut_droite = zone_HD(h,w,l,eps)
bas_gauche = zone_BG(h,w,l,eps)
bas_droite = zone_BD(h,w,l,eps)
centre = zone_C(h,w,l,eps)
liste_zone = [centre,haut_gauche,haut_droite,bas_gauche,bas_droite]


x = 400
y = 500

for z in liste_zone:
    if z.in_zone(x,y):
        print("Le point (",x,",",y,") est dans la zone : ",z.get_name(),", Nb : ",z.get_zoneNb())
        break

#print("Test zone_HG : ",haut_gauche.in_zone(400,500))

rectangle_color=(0,0,255)
cv2.rectangle(frame,(0,0),((int)(w/2),(int)(h/2)),rectangle_color,2)
cv2.rectangle(frame,((int)(w/2),0),(w,(int)(h/2)),rectangle_color,2)
cv2.rectangle(frame,(0,(int)(h/2)),((int)(w/2),(int)(h/2)),rectangle_color,2)
cv2.rectangle(frame,((int)(w/2),(int)(h/2)),(w,h),rectangle_color,2)
cv2.rectangle(frame,(l,eps),(w-l,h-eps),rectangle_color,2)

print('Fenêtre de : ',h,'x',w)

while(True):
    cv2.imshow('main',frame)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()