# Cette programme affiche le nombre des valeurs positives ( alors, strictement plus grande
# que zero) dans un liste donné par l'utilisateur.

def positive(l):
    ''' paramètres (un liste) et retourne un entier

    Cet fonction utilise un boucle pour parcourir la liste donnée et compter le nombre
    des valeurs positives.'''

    num = 0
    for x in l:
        # Cet boucle parcours le liste et compare chaque élément
        # avec zéro pour verifier si l'élément est positive
        if float(x) > 0:
            # Si l'élément est plus grande que zéro, le compteur ajoute un.
            num += 1

    return num

# Ici, la program demande l'utilisateur pour une liste et convertit la chaîne des
# charactères retournée par 'input' dans une liste
liste = list(eval(input("Veuillez entrer une liste des valeurs separees par virgules: ")))

# La programme affiche le nombre des entiers positives dans la liste.
print(positive(liste))
