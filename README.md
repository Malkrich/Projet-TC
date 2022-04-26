# Projet de tronc commun : programme de traitement de l'image

## Pré traitement

Le pré-traitement est constitué de __2 grandes étapes__

### 1) récupération de la couleur rouge saturé
Pour cela, on commence par un seuillage des 3 canaux RGB. Le seuillage pour le canal rouge est plus élevé afin de récupérer le rouge le plus saturé possible.
On effectue ensuite des opérations logiques afin d'obtenir une image uniquement avec les informations intéressante. On commence par faire un __et__ logique sur le vert et le bleu pour obtenir les éléments à éliminer. On effectue ensuite un __et__ logique entre l'image précédente en __non__ (ce qui est à 1 passe à 0 et inversement) et le rouge. On récupềre ainsi la couleur rouge.
En résumé : resultat = red && not(blue && green).

### 2) élimination du bruit
Pour cela, on effectue une simple érosion sur l'image pour éliminer les petit pixel isolés.
On utilise un élément structurant circulaire de 10x10 pixels. Cela permet de récupérer les formes nécessaires


## Détection des contours

Pour détecter les contours, on utilise les fonctions de la librairie *CV2*. __2 en particulier__.

### 1) cv2.findContour()
Elle permet de faire un contour avec des points à partir d'une image binaire. Ces contours contiennent souvent beaucoup de points.

### 2) cv2.approxPolyDP()
Cette fonction permet d'approximer les contours dessinés. Cela permet de récupérer une simple forme avec peu de points. Connaissant le nombre de points qui entoure la forme, on peut alors en déduire quelle forme il s'agit.
