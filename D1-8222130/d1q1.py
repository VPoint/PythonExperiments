
#Initialiser les variables
livres = float(input("Entrez le nombre de livres: "))
onces = float(input("Entrez le nombre d'onces: "))

#Faire la conversion
kg = livres*0.453592 + onces*0.0283495

#Emprimer
print( livres, "livres et", onces ,"onces équivalent à", kg, "kilogrammes")
