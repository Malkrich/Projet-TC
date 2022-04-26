import numpy as np
import cv2
import imutils

from class_form import form


def get_red(img):
    """ Solution RGB """
    blue_c = img[:,:,0]
    green_c = img[:,:,1]
    red_c = img[:,:,2]
    ret_b, blue = cv2.threshold(blue_c,200,255,0)
    ret_g, green = cv2.threshold(green_c,200,255,0)
    ret_r, red = cv2.threshold(red_c,240,255,0)

    # on fait : /(blue && green) && red
    color_to_detect = red
    elim = np.logical_and(blue,green)
    result = np.logical_and(color_to_detect,np.logical_not(elim))
    result.dtype = 'uint8'
    result = result*255
    
    # erosion pour retirer le bruit
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
    erosion = cv2.erode(result,kernel,iterations=1)
    
    """ Solution HSV """
    #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #teinte_basse = np.array([110,0,0])
    #teinte_haute = np.array([130,120,255])
    #blue = cv2.inRange(hsv, teinte_basse, teinte_haute)
    #cv2.imshow('blue',blue)
    
    return erosion

def contours_detection(img):
    cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    return cnts
    

# lancement capture vidéo
cap = cv2.VideoCapture(0)

f = form()

# lecture frame par frame
while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    # opérations
    logical_img = get_red(frame)
    
    # detection de contours
    cnts = contours_detection(logical_img)
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        cv2.drawContours(frame, [approx], -1, (0,255,0), 3)
        f.set_sommets(len(approx))
        f.display_info()
    
    cv2.imshow('contours',frame)
    
    
    # on appuis sur q pour quitter
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()