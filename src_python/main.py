import numpy as np
import cv2
import imutils

def get_blue(img):
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    teinte_basse = np.array([160,220,0])
    teinte_haute = np.array([180,255,255])
    blue = cv2.inRange(hsv, teinte_basse, teinte_haute)
    
    return blue

def contours_detection(img):
    cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
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
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # nuances de gris
    blue = get_blue(frame)
    #ret, thresh = cv2.threshold(blue, 127, 255, 0)
    
    # detection de contours
    cnts = contours_detection(blue)
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    
    cv2.drawContours(blue, [approx], -1, (0,255,0), 3)
    cv2.imshow('contours',blue)
    
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()