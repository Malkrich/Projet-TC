import numpy as np
import cv2
import imutils

def shape_detection(img):
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
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    thresh = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)[1]
    
    # Display
    cv2.imshow('frame',thresh)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()