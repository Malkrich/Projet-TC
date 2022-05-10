import cv2

class form:
    # attribut du nombre de sommet et du nom du polygone
    sommets = 0
    pol = 'undefined'
    cX = 0
    cY = 0
    
    # collection des polygones pour en selectionner un
    collec_poly = {
        3 : 'triangle',
        4 : 'rectangle',
        5 : 'pentagone',
        6 : 'hexagone',
        }
    
    def __init__(self):
        print('ajout instance class form')
    
    def set_forme(self,s):
        #calcul du nombre de sommets
        self.sommets = len(s)
        self.pol = self.collec_poly.get(self.sommets,'undefined')

        # calcul du centre
        M = cv2.moments(s)
        try:
            self.cX = int(M["m10"]/M["m00"])
            self.cY = int(M["m01"]/M["m00"])
        except:
            print("division par 0")
            self.cX=0
            self.cY=0
            
    def clear_forme(self):
        self.sommets = 0
        self.pol = 'undefined'
            
    def get_centre(self):
        return self.cX,self.cY
    
    def forme_exist(self):
        ret = False
        if self.pol != 'undefined':
            ret = True
        return ret
    
    # fonction de test
    def display_info(self):
        if self.forme_exist():
            print('Forme : ',self.pol,", au coordonnées : (",self.cX,",",self.cY,")")