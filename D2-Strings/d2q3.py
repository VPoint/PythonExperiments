# Cette program servira d’outil d’apprentissage d’opérations arithmétiques pour les élèves
# de l’école élémentaire. Le logiciel permet à l’élève de choisir l’opération arithmétique
# qu’il ou elle veut pratiquer. L’élève choisit l’une de deux opérations, soit la
# multiplication, soit l’addition. Selon le choix effectué, le logiciel teste l’élève avec
# un exercice contenant exactement 10 questions.

import random

# Partie A:
def opérations(a):
    # Définir un variable pour le nombre des bonnes réponses
    bonAns = 0

    # Afficher les instrictions
    print('SVP donnez les reponses aux questions suivantes: ')

    # Commencer un boucle pour génèrer les 10 questions
    for i in range(0,10):
        # Génerer deux nombres aléatoires
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)

        # Choisir l'opération arithmétique
        if(a == 0):
            # Vérifier si l'opération est l'addition
            opération = '+'
            vAns = n1 + n2
        elif(a == 1):
            # Vérifier si l'opération est la multiplication
            opération = 'x'
            vAns = n1*n2

        # Demander la réponse du utilisateur 
        uAns = int(input(str(n1)+ ' ' + opération + ' ' + str(n2) + ' = '))

        if(vAns == uAns):
            # Si la réponse est bonne, ajouter un au nombre des bonnes réponses
            bonAns += 1
        else:
            # Sinon, emprimmer la bonne réponse
            print('Incorrect – la reponse est ', vAns)

    # Rétourner la nombre des bonnes réponses
    return bonAns

# Partie B:

# Emprimer l'introduction
print('Ce logiciel va effectuez un test avec 10 questions.')

# Demander l'utilaseur de choissir l'opération
genre = int(input('SVP choisisser l\'operation 0) Addition 1) Multiplication (0 ou 1): '))

# Appelle la fonction pour fabriquer le test
correct = opérations(genre)
    
# Publier le nombre des boonnes réponses
print(correct, ' réponses correctes.')
    
if(correct > 6):
    # S'il y a plus que 6 bonnes réponses envoie 'Félicitations'
    print('Félicitations')
else:
    # Sinon, afficher la message suivant:
    print('Demandez à votre enseignant(e) de vous aider')
