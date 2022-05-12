

"""
Tram :
    Préfixe :
        - m : servomoteur
        - l : lampe
    
    Moteurs :
        - a/r/d/g : avancer/reculer/droite/gauche
        - x : arreter
    
    Lampe :
        - x : rien faire, mode normal
        - ccX,cY : demande de ciblage, envoie c + coord_x,coord_y
"""

collec_zone = {
    0 : 'hg',
    1 : 'hd', 
    2 : 'bg',
    3 : 'bd',
    4 : 'c'
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
    
def send_message_lamp(mode,cX,cY):
    ret = 'lx'
    
    if mode == 'c':
        ret = 'lc'+cX+','+cY
    
    return ret

def read_data(ser):
    data = ""
    current_data = ""
    while current_data != "x":
        current_data = ser.read().decode()
        data += current_data

    return data