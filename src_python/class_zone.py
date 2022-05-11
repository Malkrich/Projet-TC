class zone:
    zone = 0
    
    def __init__(self,h_param,w_param,l_param,eps_param):
        self.h = h_param
        self.w = w_param
        self.l = l_param
        self.eps = eps_param
        self.zoneNb = -1
        self.name = ''
        
    def get_zoneNb(self):
        return self.zoneNb
    
    def get_name(self):
        return self.name
    
    def in_zone(self,x,y):
        return False

class zone_HG(zone):
    def __init__(self,h_param,w_param,l_param,eps_param):
        super().__init__(h_param,w_param,l_param,eps_param)
        self.zoneNb = 0
        self.name = "haut gauche"
        print("ajout instance class zone_HG")
        
    def in_zone(self,x,y):
        ret = False
        if x < (int)(self.w/2) and y < (int)(self.h/2):
            ret = True
        return ret
        
    
class zone_HD(zone):
    def __init__(self,h_param,w_param,l_param,eps_param):
        super().__init__(h_param,w_param,l_param,eps_param)
        self.zoneNb = 1
        self.name = "haut droite"
        print("ajout instance class zone_HD")
        
    def in_zone(self,x,y):
        ret = False
        if x > (int)(self.w/2) and y < (int)(self.h/2):
            ret = True
        return ret
        
class zone_BG(zone):
    def __init__(self,h_param,w_param,l_param,eps_param):
        super().__init__(h_param,w_param,l_param,eps_param)
        self.zoneNb = 2
        self.name = "bas gauche"
        print("ajout instance class zone_BG")
        
    def in_zone(self,x,y):
        ret = False
        if x < (int)(self.w/2) and y > (int)(self.h/2):
            ret = True
        return ret
        
class zone_BD(zone):
    def __init__(self,h_param,w_param,l_param,eps_param):
        super().__init__(h_param,w_param,l_param,eps_param)
        self.zoneNb = 3
        self.name = "bas droite"
        print("ajout instance class zone_BD")
        
    def in_zone(self,x,y):
        ret = False
        if x > (int)(self.w/2) and y > (int)(self.h/2):
            ret = True
        return ret
        
class zone_C(zone):
    def __init__(self,h_param,w_param,l_param,eps_param):
        super().__init__(h_param,w_param,l_param,eps_param)
        self.zoneNb = 4
        self.name = "centre"
        print("ajout instance class zone_C")
        
    def in_zone(self,x,y):
        ret = False
        if x > self.l and x < (self.w-self.l) and y > self.eps and y < (self.h-self.eps):
            ret = True
        return ret