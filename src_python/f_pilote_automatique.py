from tkinter import N
import numpy as np
import cv2

from uart import send_message_motor



#           Declaration des variables
nb_cible = 4
nb_cible_touche= 0
coord_init = [1,1]
coord_actuelle = [1,1]
orientation_actuelle = 0
distance_decalage = 2
compteur_exploration = 1
taille_map=10
distance_min_mvmt=1

M=np.zeros((taille_map,taille_map)) 
M[0][1]=1
M[1][0]=1
N=[[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,1,1,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,0,0,0,1,1],
[1,0,0,1,1,0,0,1,1,1],
[1,0,0,0,0,0,0,0,1,1],
[1,1,1,0,0,1,1,0,0,1],
[1,0,0,0,0,1,1,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]]

            



#          Creation de 3 fonctions obstacles

def obstacle_gauche(distance):
    ret = False
    if distance <= 30:
        ret = True
        
    return ret

def obstacle_droite(distance):
    ret = False
    if distance <= 30:
        ret = True
        
    return ret

def obstacle_avant(distance):
    ret = False
    if distance <= 30:
        ret = True
        
    return ret


#      Recuperation des fonctions de base (avancer,tourner,...)

def virage_droite():
    print("virage droite")

    orientation(1)
    
    return send_message_motor('right')
    #return "digo 1:550:70 2:-550:70\r"

def virage_gauche():
    print("virage gauche")
    
    orientation(-1)
    
    return send_message_motor('left')
    #return "digo 1:-550:70 2:550:70\r"

def avancer():
    print("avancer")
    
    global orientation_actuelle
    if orientation_actuelle == 0:
        coord_actuelle[1]+=1
    elif orientation_actuelle == 1:
        coord_actuelle[0]+=1
    elif orientation_actuelle ==2 :
        coord_actuelle[1]-=1
    else :
        coord_actuelle[0]-=1
    return send_messsage_motor('front')
    #return "mogo 1:-30 2:-30\r"


#           fonction de base

def orientation(p):
    global orientation_actuelle
    if orientation_actuelle==3 and p==1:
       orientation_actuelle = 0
    elif orientation_actuelle==0 and p==-1:
        orientation_actuelle = 3
    else :
         orientation_actuelle += p
    return

def premier_tour(distance):
    if obstacle_gauche(distance):
        maj_obstacle_gauche()
        if obstacle_avant(distance):
            maj_obstacle_avant()
            virage_droite()
            avancer()
        else :
            avancer()
    else:
        virage_gauche()
        avancer()


def mise_en_position():
    global compteur_exploration
    if compteur_exploration == 1:
        virage_droite()
        virage_droite()
    else :
        virage_gauche()
    while coord_actuelle[0]!=coord_init[0]+compteur_exploration*distance_decalage:
        if obstacle_droite():
            maj_obstacle_droite()
            if obstacle_avant():
                maj_obstacle_avant()
                virage_gauche()
                avancer()
            else: 
                avancer()
        else:
            virage_droite()
            avancer()
    virage_gauche()
    return np.copy(coord_actuelle)
    
def obstacle_fond():
    for i in range(coord_actuelle[0]-1+distance_min_mvmt,coord_actuelle[0]+distance_min_mvmt):
        ymin=np.copy(taille_map)
        for j in range(taille_map//2,taille_map):
           if M[i][j]==1:
               if ymin>j:
                   ymin=j
    return taille_map-ymin


def maj_obstacle_gauche():
    if orientation_actuelle == 0:
        M[coord_actuelle[0]-1][coord_actuelle[1]]=1
    elif orientation_actuelle == 1:
         M[coord_actuelle[0]][coord_actuelle[1]+1]=1
    elif orientation_actuelle == 2:
        M[coord_actuelle[0]+1][coord_actuelle[1]]=1
    else :
         M[coord_actuelle[0]][coord_actuelle[1]-1]=1
    return

def maj_obstacle_droite():
    if orientation_actuelle == 0:
        M[coord_actuelle[0]+1][coord_actuelle[1]]=1
    elif orientation_actuelle == 1:
         M[coord_actuelle[0]][coord_actuelle[1]-1]=1
    elif orientation_actuelle == 2:
        M[coord_actuelle[0]-1][coord_actuelle[1]]=1
    else :
         M[coord_actuelle[0]][coord_actuelle[1]+1]=1
    return

def maj_obstacle_avant():
    if orientation_actuelle == 0:
        M[coord_actuelle[0]][coord_actuelle[1]+1]=1
    elif orientation_actuelle == 1:
         M[coord_actuelle[0]+1][coord_actuelle[1]]=1
    elif orientation_actuelle == 2:
        M[coord_actuelle[0]][coord_actuelle[1]-1]=1
    else :
         M[coord_actuelle[0]-1][coord_actuelle[1]]=1
    return


def contournement(x):
    if obstacle_gauche():
        maj_obstacle_gauche()
        virage_gauche()
        virage_gauche()
        avancer()
        while obstacle_droite():
            maj_obstacle_droite()
            avancer()
        virage_droite()
        avancer()
    else :
        virage_gauche()
        avancer()
    while coord_actuelle[0]!=x:
        if obstacle_avant() and obstacle_droite():
            maj_obstacle_avant()
            virage_gauche() 
            avancer()
            while obstacle_droite():
                maj_obstacle_droite()
                avancer()
            virage_droite()
            avancer()
        elif obstacle_droite():
            maj_obstacle_droite()
            avancer()
        else : 
            virage_droite()
            avancer()
    virage_gauche()
    return
            

            


def exploration_allez(coord):
    avancer()
    while coord_actuelle[1]<taille_map-1-obstacle_fond():
        if obstacle_avant():
            maj_obstacle_avant()
            contournement(coord[0])
        else:
            avancer()
    virage_droite()
    virage_droite()
    return

def exploration_retour(coord):
    while coord_actuelle[1]>coord[1]:
        if obstacle_avant()==True:
            maj_obstacle_avant()
            contournement(coord[0])
        else:
            avancer()
    while obstacle_avant()==False:
        avancer()
    return

def deuxieme_tour():
    global compteur_exploration
    coord_utile=[0,0]
    for i in range((taille_map-2)//distance_decalage-1):
        coord_utile=mise_en_position()
        exploration_allez(coord_utile)
        exploration_retour(coord_utile)
        compteur_exploration+=1
    return



# test global

#premier_tour()
#deuxieme_tour()

#M=M*255
#cv2.imwrite('carto.png',M)

#cv2.imwrite('carto2.png',N)



#      Test pour premier tour 

"""    
def obstacle_gauche(i):
    paterne = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1]
    if paterne[i]==1:
        return True
    else :
        return False

def obstacle_droite(k):
    paterne3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1]
    if paterne3[k]==1:
        return True
    else :
        return False
def obstacle_avant(j):
    paterne2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]
    if paterne2[j]==1:
        return True
    else :
        return False
"""





#          Test mise en position


"""

orientation_actuelle=3


def obstacle_gauche(i):
    paterne = [0,0,0,0,0,0,0,0]
    if paterne[i]==1:
        return True
    else :
        return False

def obstacle_droite(k):
    paterne3 = [1,1,1,1,1,1,0,1]
    if paterne3[k]==1:
        return True
    else :
        return False
def obstacle_avant(j):
    paterne2 = [0,0,0,0,1,0,0]
    if paterne2[j]==1:
        return True
    else :
        return False

"""