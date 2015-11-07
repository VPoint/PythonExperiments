#Initialiser les variables
livres = float(input("Entrez le nombre de livres: "))
onces = float(input("Entrez le nombre d'onces: "))

def changeKg(lb, ou):
    'Faire la conversion'
    ans = lb*0.453592 + ou*0.0283495
    return ans

#Appeler la fonction
kg = changeKg(livres, onces)

#Emprimer
print( livres, "livres et", onces ,"onces équivalent à", kg, "kilogrammes")
