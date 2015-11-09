# Cette program servira d’outil d’apprentissage d’opérations arithmétiques pour les élèves
# de l’école élémentaire. Le logiciel génère l’opération arithmétique d'une manière
# aléatoire soit la multiplication, soit l’addition et l'élève entre la réponse. Selon le
# choix effectué, le logiciel teste l’élève avec un exercice contenant exactement 10
# questions.

import random

# Partie A:
def opérations(a):    
    # Génerer deux nombres aléatoires
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)

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
        # Retourner vrai si la réponse tapé est bonne
        return True
    else:
        # Si non, retourner faux et emprimer la bonne réponse
        print('Incorrect – la reponse est', vAns)
        return False

# Partie B:

# Définir un conteur pour le nombre des réponses correctes
bonAns = 0

# Emprimer l'introduction
print('Ce logiciel va effectuez un test avec 10 questions.')

# Commencer un boucle pour génèrer les 10 questions
for n in range(0,10):
    # Génèrer un entier de 0 ou 1
    genre = random.randint(0, 1)

    # Puis appelle la fonction utilisant l'entier aléatoire
    if(opérations(genre)):
        # S'il rétourne 'Vrai' ajouter 1 au nombre des bonnes réponses
        bonAns += 1

# Publier le nombre des boonnes réponses
print(bonAns, ' réponses correctes.')
    
if(bonAns > 6):
    # S'il y a plus que 6 bonnes réponses envoie 'Félicitations'
    print('Félicitations')
else:
    # Sinon, afficher la message suivant:
    print('Demandez à votre enseignant(e) de vous aider')
