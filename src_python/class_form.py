

class form:
    poly = {
        3 : 'triangle',
        4 : 'rectangle',
        5 : 'pentagone',
        6 : 'hexagone',
        }
    
    def __init__(self):
        self.sommets = 0
    
    def set_sommets(self,s):
        self.sommets = s
    
        
    # fonction de test
    def display_info(self):
        print(self.poly.get(self.sommets,'undefined'))