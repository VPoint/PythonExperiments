# Cette programme convertit les nombre romaines utilisant M, D, C, X, V, I en nombres réels.
# Les règles des nombres romaines était simplifié pour éviter la confusion (alors IV serait
# évalué comme VI). Le programme principal devrait lire un nombre romain du clavier, appeler
# la fonction de a), afficher son résultat, et aussi appeler la fonction de b) et afficher
# son résultat.

#Partie A : Utilisant les méthodes qui s’appliquent sur des chaînes de caractères
#           (de la classe str).
def romaine_v1(ch):
    ''' paramètres (chaîne de charactères) et retourn int

    Cette function utilise la méthode .count dans la classe str et conte le nombre de chaque
    lettre dans le nombre romaine. Utilisant la multiplication il est alors possible de
    calculer le nombre réel.'''

    # Le programme déclare les variables pour retenir le nombre de chaque lettre
    nM = ch.count('M')
    nD = ch.count('D')
    nC = ch.count('C')
    nX = ch.count('X')
    nV = ch.count('V')
    nI = ch.count('I')

    # Cette equation multiplie le nombre des variables par leur valeur actuelle et
    # ajoute toutes les nombres ensemble pour faire un seul nombre
    nombre = nM*1000 + nD*500 + nC*100 + nX*10 + nV*5 + nI

    # Le fonction return le nombre réel
    return nombre

# Partie B : Utilisant une boucle.
def romaine_v2(ch):
    ''' paramètres (chaîne de charactères) et retourn int

    Cette function utilise un boucle pour verifier la présence de chaque lettre dans le
    nombre romaine. Lorsqu'un chiffre romaine est trouvé, la fonction ajoute cette valeur
    réel au total. Utilisant l'addition il est possible de calculer le nombre réel.'''

    # La variable pour le nombre réel est défini
    nombre = 0

    # Le boucle traverse la chaîne des charactères et verifie chaque lettre contre les
    # chiffres romaines. Si'il est vrai, on ajoute la valeur réel au total réel.
    # Si non, rien arrive.
    for l in ch:
        if l == 'M':
            nombre += 1000
        elif l == 'D':
            nombre += 500
        elif l == 'C':
            nombre += 100
        elif l == 'X':
            nombre += 10
        elif l == 'V':
            nombre += 5
        elif l == 'I':
            nombre += 1
    
    # Le fonction return le nombre réel
    return nombre


# Ici, la program demande l'utilisateur pour un nombre romain du clavier
romNum = input("Entrez un nombre romain en utilisant les lettres M, D, C, X et I:")

# Le programme appelle chaque fonction et retourne la résultat
# Le premier fonction utilise les modules définies
print(romaine_v1(romNum))
# Le deuxième fonction utilise un boucle
print(romaine_v2(romNum))
