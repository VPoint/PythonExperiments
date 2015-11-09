# Cette programme change la liste donné par l'utilisateur pour que les éléments soient en
# ordre inverse. Il affiche la nouvelle liste.

def inverse(l):
    ''' paramètres (un liste) et retourne rien

    Cet fonction utilise un boucle pour parcourir la liste donnée et changer l'ordre
    des éléments à l'inverse'''

    # Cette condition verifie si la liste a un longeur paire
    if(len(l)% 2 == 0):
        # Si oui, toutes les éléments sont échangés
        c = 0

        # Cette boucle parcours un demi de la liste
        while (c < len(l)/2):
            # Ici on définit un variable intermédiare pour garder le valeur
            # initial
            temp = l[c]
            # On échange la valeur avec celui au fin du liste
            l[c] = l[(len(l)-1)-c]
            # On met le valeur initiale au fin du liste
            l[(len(l)-1)-c] = temp

            # Le compteur incrément par un
            c += 1
    else:
        # Si non, la valeur au millieu n'est pas changé
        c = 0
        # Cette boucle parcours seulment un demi de la liste sauf le valeur
        # au millieu
        while (c <(len(l)-1)/2):
            # Ici on définit un variable intermédiare pour garder le valeur
            # initial
            temp = l[c]
            # On échange la valeur avec celui au fin du liste
            l[c] = l[(len(l)-1)-c]
            # On met le valeur initiale au fin du liste
            l[(len(l)-1)-c] = temp
            # Le compteur incrément par un
            c += 1
        
# Ici, la program demande l'utilisateur pour une liste et convertit la chaîne des
# charactères retournés par 'input' dans une liste
liste = list(eval(input("Veuillez entrer une liste des valeurs separees par virgules: ")))

inverse(liste)

# La programme affiche la liste dans l'ordre inverse.
print(liste)
