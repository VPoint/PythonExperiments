########################### Exercise 1 #######################
print("************************** Exercise 1 *************************")

compteur = 10
while(compteur > 0):
 print(compteur)
 compteur = compteur - 1

########################### Exercise 2 #######################
print("************************** Exercise 2 *************************")

N = int(input("SVP tapez un nombre: "))

compteur = 1
while (compteur <= N):
    print(compteur, end = " ")
    compteur += 1
print("*** Avec 'while' ****")

for i in range(1, N+1):
    print (i, end = " ")
print("*** Avec 'for' ****")

########################### Exercise 3 #######################
print("************************** Exercise 3 *************************")
import random

print("Un jeu de denvinette!!")
x = random.randint(1,10)
y = int(input("Diviner le nombre entre 10 et 1: "))

def devine(a, b):
    compteur = 1;
    while(a != b):
        if(b > a):
            print("Trop Haut!")
            b = int(input("Essayez encore!: "))
        else:
            print("Trop Bas!")
            b = int(input("Essayez encore!: "))
        compteur += 1;

    return 'Success!! Tu as pris ' + str(compteur) + ' tentatives pour trouver le nombre.'

print(devine(x, y))

########################### Exercise 4 #######################
print("************************** Exercise 4 *************************")
num = int(input('SVP tapez un entier plus grand que zero:'))

while (num == 0) or (num < 0):
    print('Ton nombre n\'est pas plus grande que zero.')
    num = int(input('SVP tapez un nouveau entier plus grand que zero:'))

def calculeFact(f):
    fact = 1
    for i in range(1, f + 1):
        fact = fact*i;
    return fact

print (calculeFact(num))    
