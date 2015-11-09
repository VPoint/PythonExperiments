# Cette programme affiche une booléen qui verifie si toutes les nombres dans un liste
# donné par l'utilisateur sont positives.

def toutPositive(l):
    ''' paramètres (un liste) et retourne un booléen (True si toutes les nombres sont
    positives et False si au moins un nombre est négative)

    Cet fonction utilise un boucle pour parcourir la liste donnée et verifier si les
    nombres sont positives'''

    for x in l:
        # Cet boucle parcours le liste et compare chaque élément
        # avec zéro pour verifier si l'élément est positive
        if float(x) <= 0:
            # Si un élément est plus petit ou égal à zéro, toutes les nombres du liste
            # ne sont pas positives et on retourne False
            return False

    # Si la condition dans le boucle est jamais vrai, il veut dire que toutes les
    # éléments dans la liste sont plus grande que 0.
    return True

# Ici, la program demande l'utilisateur pour une liste et convertit la chaîne des
# charactères retournés par 'input' dans une liste
liste = list(eval(input("Veuillez entrer une liste des valeurs separees par virgules: ")))

# La programme affiche une booléen qui réprésent si la liste est positive.
print(toutPositive(liste))
