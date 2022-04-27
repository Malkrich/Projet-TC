

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
    
    def set_forme(self,s):
        self.sommets = s
        self.pol = self.collec_poly.get(self.sommets,'undefined')
    
    def forme_exist(self):
        ret = False
        if self.pol != 'undefined':
            ret = True

        return ret
    
    # fonction de test
    def display_info(self):
        if self.forme_exist():
            print('J ai trouve une forme : ',self.pol)