

class form:
    # attribut du nombre de sommet et du nom du polygone
    sommets = 0
    pol = 'undefined'
    
    # collection des polygones pour en selectionner un
    collec_poly = {
        3 : 'triangle',
        4 : 'rectangle',
        5 : 'pentagone',
        6 : 'hexagone',
        }
    
    def __init__(self):
        print('ajout instance class form')
    
    def set_sommets(self,s):
        self.sommets = s
        self.get_form()
    
    def get_form(self):
        self.pol = self.collec_poly.get(self.sommets,'undefined')
        
    # fonction de test
    def display_info(self):
        print(self.pol)