# Cette programme prends un chaîne des charactères écrit par l'usager et retourne un
# chaîne modifié. La programme modifie la chaîne en doublant chaque lettre et mettant
# la chaîne en ordre inverse. Cette chaîne modifié est alors affiché sur l'écran.

def doubleInverse(ch):
    ''' paramètres (un chaîne des charactère) et retourne un chaîne des
    charactères modifié

    Cet fonction utilise un boucle pour parcourir la liste donnée et changer l'ordre
    des éléments à l'inverse et en doublant.'''

    rs = ''
    # Cette boucle parcours le chaîne des charactères 
    for x in range(1, len(ch)+1):
        # Cette procèdure concatenait les lettres dans l'ordre inverse et doublé
        rs += ch[-x]*2
    
    return rs
        
# Ici, la program demande l'utilisateur pour un chaine dees charactères
s = input("Veuillez entrer une phrase: ")

# La programme affiche la chaîne des charactèeres doublé dans l'ordre inverse.
print(doubleInverse(s))
