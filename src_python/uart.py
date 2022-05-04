"""
Tram :
    Préfixe :
        - M : servomoteur
        - L : lampe
    
    Moteurs :
    
    Lampe :
        1) H/B : haut/bas
        2) G/D/C : gauche/droite/centre

    En fin de chaine : +"X"
"""

collec_zone = {
    0 : 'HG',
    1 : 'HD',
    2 : 'BG',
    3 : 'BD',
    4 : 'C'
}

def send_message_motor():
    print("send message tout motor")
    
def send_message_lamp(zone):
    ret = "L" + collec_zone.get(zone,'') + "X"
    return ret