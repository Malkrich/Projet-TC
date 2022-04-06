import numpy as np
import cv2
import imutils

    

# lancement capture vidéo
cap = cv2.VideoCapture(0)

# lecture frame by frame
while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    # opérations
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    thresh = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    # Display
    cv2.imshow('frame',thresh)
    #cv2.imshow('gray',gray)
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()