# Cette program calcule l’indice de masse corporelle (IMC)

def calcIMC(poids, taille):
    'Cette fonction calcule l\'indice de la masse corporelle.'
    ans = poids/(taille**2) #le poids en kg divisé par la taille en mètres, au carré
    return ans

# L'usager entre son poids et sa taille
kg = float(input('SVP entre ton poids en kg: '))
m = float(input('SVP entre ton taille en mètres: '))

# La programme appelle la fontion pour calculer le IMC
IMC = calcIMC(kg, m)

print('Votre IMC est ', IMC)

# La programme compare entre les valeurs pour afficher le bon message
if(IMC < 18.5):
    # Si l'IMC est plus petit que 18.5, l'usager est trop mince
    print('Maigreur')
elif(IMC >= 18.5 and IMC < 25):
    # Si l'IMC est entre 18.5(inclue) et 25(exclue), l'usager est saine
    print('Poids idéal')
elif(IMC >= 25 and IMC < 30):
    # Si l'IMC est entre 25(inclue) et 30(exclue), l'usager est classifié comme surpoids
    print('Surpoids')
else:
    # Si l'IMC est plus grande que 30(inclue), l'usager est obesse
    print('Obésité')
