import numpy as np
import cv2
import imutils

def contours_detection(img):
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    return cnts
    

# lancement capture vidéo
cap = cv2.VideoCapture(0)

# lecture frame by frame
while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    # opérations
    # pre traitement
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    
    cnts = contours_detection(thresh)
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    
    cv2.drawContours(thresh, [approx], -1, (0,255,0), 3)
    cv2.imshow('contours',thresh)
    
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()