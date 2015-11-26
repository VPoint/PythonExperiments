def ajoute(m):
    ''' Cette fonction accepte des matrices et retourne rien.
    Pour chaque membre du matrice, ajoutez un. Il change le matrice donnée.'''
    for x in range(len(m)):
        for h in range(len(m[x])):
            m[x][h] += 1

def ajoute_V2(m):
    ''' Cette fonction accepte des matrices et retourne un matrice modifié.
    Pour chaque membre du matrice, on ajoute un à la valeur et l'ajoute au
    matrice modifié. Il ne change pas le matrice donnée.'''
    retM = [[] for j in m]
    for x in range(len(m)):
        for h in range(len(m[x])):
            retM[x].append(m[x][h] + 1)

    return retM

# SVP entrez le matrice comme une liste des listes (ex: [[],[],[]])
matrice = list(eval(input('SVP Entrez un matrice:')))
print('Ton matrice:',matrice)

m2 = ajoute_V2(matrice)
print('Un nouveau matice avec les éléments ajouté par un:',m2)
print('Ton matrice original:', matrice)

# Car ajoute change les éléments du matrice, il vient après celui qui
# ne change pas le matrice d'origine
ajoute (matrice)
print('Ton matrice original modifié:', matrice)
