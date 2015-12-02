# a) fonction récurisve qui imprime des étoiles

def etoiles(c):
    #c = le nombre d'étoiles à afficher
    e = "*"
    if c <= 0:
        yo =1 #fait rien, besoin d'une ligne de code ici, condition pour arrêter d'invoquer de nouveau la fonction
    else:
        print(c*e) #imprime le premier set d'étoiles
        etoiles(c-1) #appel récursif
        print(c*e) #imprime deuxième set d'étoiles

# b) fonction récursive qui donne la somme des éléments positif dans la liste

def sommeListePos_rec(l, n):
    # l est la liste, n sa longueur
    somme = 0 #initialise la somme
    if n > 1: #condition de base
        somme = somme + sommeListePos_rec(l, n-1) #l'ajout de la somme avec la nouvelle somme partielle
        
        
    if l[n-1] >0: #test pour vérifier si un nombre est positif
        return l[n-1] + somme #si oui, on l'ajoute à la somme partielle
    else:
        return 0 + somme #sinon, on ne retourne que la somme partielle    
