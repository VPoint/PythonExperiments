#Initialiser les variables des données et mettes le en cents
total = float(input("Entrez le montant en dollars: "))*100

def contezLesPièces(total):
    #Initialiser les variables
    sous25, sous10, sous5, sous1 = 0,0,0,0

    #Trouver le nombre de 25 sous
    sous25 = total//25

    #Trouver le nombre des 10 sous
    total = total%25
    sous10 = total//10

    #Trouver le nombre des 5 sous
    total = total%10
    sous5 = total//5

    #Trouver le nombre des 1 sous
    total = total%5
    sous1 = total//1

    #Additioner tout les pièces ensemble
    sousTotal = sous25 + sous10 + sous5 + sous1

    print("Le nombre minimal de pièces que le caissier peut rendre est:", sousTotal)

#Appeler la fonction
contezLesPièces(cout)
