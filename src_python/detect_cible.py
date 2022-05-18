import numpy as np
import cv2
import imutils


def get_red(img):
    """ Solution RGB """
    blue_c = img[:,:,0]
    green_c = img[:,:,1]
    red_c = img[:,:,2]
    ret_b, blue = cv2.threshold(blue_c,70,255,0)
    ret_g, green = cv2.threshold(green_c,70,255,0)
    ret_r, red = cv2.threshold(red_c,170,255,0)

    # on fait : /(blue && green) && red
    color_to_detect = red
    elim = np.logical_and(blue,green)
    result = np.logical_and(color_to_detect,np.logical_not(elim))
    result.dtype = 'uint8'
    result = result*255
    
    # erosion pour retirer le bruit
    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
    kernel = None
    erosion = cv2.erode(result,kernel,iterations=2)
    dilatation = cv2.dilate(erosion,kernel,iterations=2)
    
    return erosion

    #cv2.imshow('dilatation',dilatation)
    
    """ Solution HSV

    - hue compris dans l'interval [0,179]
    saturation et value dans l'interval [0,255]"""
    #red_c = img[:,:,2]
    #red_th = cv2.morphologyEx(red_c,cv2.MORPH_OPEN,None,iterations=5)
    #cv2.imshow('red',red_th)
    #img[:,:,2] = red_th
    
    """hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    teinte_basse = (170,100,100)
    teinte_haute = (179,180,255)
    red = cv2.inRange(hsv, teinte_basse, teinte_haute)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
    ouverture = cv2.morphologyEx(red,cv2.MORPH_OPEN,kernel,iterations=1)
    dilatation = cv2.dilate(ouverture,None,iterations=1)
    
    cv2.imshow('dilatation',dilatation)
    return dilatation"""

def contours_detection(img):
    cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    return cnts

def main_contour(frame):    
    # pre traitement
    logical_img = get_red(frame)
    
    # detection de contours
    cnts = contours_detection(logical_img)
    
    return cnts