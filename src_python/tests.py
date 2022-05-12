import cv2
import numpy as np

from detect_cible import main_contour
from class_form import form

cap = cv2.VideoCapture(0)
f = form()

while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    cnts = main_contour(frame)
    
    f.clear_forme()
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.05 * peri, True)
        cv2.drawContours(frame, [approx], -1, (0,255,0), 3)
        f.set_forme(approx)
        
        # affichage non nécessaire
        cX,cY = f.get_centre()
        cv2.circle(frame,(cX,cY),4,(0,255,0),-1)
        centre_str = str(cX) + ',' + str(cY)
        cv2.putText(frame, centre_str, (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),2)
        #f.display_info()
        
    cv2.imshow('contours',frame)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

## fin programme
cap.release()
cv2.destroyAllWindows()