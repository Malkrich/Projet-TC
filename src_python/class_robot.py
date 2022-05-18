import time

from uart import send_message_motor,send_message_lamp

class robot:
    cible = ''
    dist = 100
    
    def __init__(self):
        print("ajout instance robot")
        self.message = send_message_motor('stop')
        
    def get_message(self):
        return self.message
    
    def maj_distance(self,distance_param):
        self.dist = distance_param
    
    def maj_cible(self,cible_param):
        self.cible = cible_param
    
    def tempo(self):
        if self.message != 'ma':
            time.sleep(2)
    
    def make_decision(self):
        self.message = send_message_motor('front')
        if self.dist < 30:
            self.message = send_message_motor('left')
        
        if self.cible != '':
            self.message = self.cible