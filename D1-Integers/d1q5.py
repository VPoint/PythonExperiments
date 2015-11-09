# Partie A
# Initialiser le variable des données du clavier
années = float(input("Entrez un nombre d'années-lumière: "))

def ansEnSec(an):
    'Convertir les années-lumières en secondes-lumières'
    sec = an*365.26*24*60*60
    return sec

# Appeler la fonction
seconds = ansEnSec(années)

print("Le nombre de secondes-lumière est", seconds)

# Partie B
def secEnKm(sec):
    'Convertir les secondes-lumières on kilomètres'
    distance = sec*300000
    return distance

# Appeler la fonction
kilomètres = secEnKm(seconds)

print("La distance est", kilomètres, "km.")

# Partie C
# Initialiser les variables des données du clavier
étoile_1 = float(input("Entrez la distance de la première étoile, en années-lumières: "))
étoile_2 = float(input("Entrez la distance de la deuxième étoile, en années-lumières: "))

def trouveDistance(d1, d2):
    'Additioner les deux distances'
    d = d2 + d1
    'Appeler les deux fonctions'
    réponse = secEnKm(ansEnSec(d))
    return réponse

# Appeler la fonction
distance = trouveDistance(étoile_1, étoile_2)

print("La distance entre les deux étoiles est", distance,"km.")

