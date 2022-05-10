

"""
Tram :
    Préfixe :
        - m : servomoteur
        - L : lampe
    
    Moteurs :
        - a/r/d/g : avancer/reculer/droite/gauche
        - x : arreter
    
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

collec_direction = {
    'front' : 'a',
    'back' : 'r',
    'left' : 'l',
    'right' : 'r',
}

def send_message_motor(direction):
    ret = 'x'
    if direction != 'stop':
        ret = 'm' + collec_direction.get(direction,'')
    return ret
    
def send_message_lamp(zone):
    ret = "XL" + collec_zone.get(zone,'')
    return ret

def read_data(ser):
    data = ""
    current_data = ""
    while current_data != "x":
        current_data = ser.read().decode()
        data += current_data

    return data