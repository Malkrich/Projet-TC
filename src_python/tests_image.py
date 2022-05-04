import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# calcul hauteur, largeur
ret, frame = cap.read()
h = len(frame)
w = len(frame[0])
l = (int)(w/3)
eps = (int)(h/3)

cnts = [[0,0],[w/2,0],[w/2,h/2],[0,h/2]]
rectangle_color=(0,0,255)
#cv2.drawContours(frame, [cnts], -1, (0,255,0), 3)
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