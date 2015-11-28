########################### Excercise 1 #######################
print("************************** Excersise 1 *************************")

def check(age):
    if(age >= 18 and age <= 55):
        return 'Transaction acceptée'
    else:
        return 'Transaction refusée'

monAge = int(input('Quel âge as-tu?'))
print(check(monAge))

########################### Excercise 2 #######################
print("************************** Excersise 2 *************************")

def actTemp(temp):
    b =0
    if (temp >= 80):
        b = 1
    elif (60 <= temp and temp < 80):
        b = 2
    elif (40 <= temp and temp < 60):
        b = 3
    else:
        b = 4

    if b == 1:
        return "1: Natation"
    elif b == 2:
        return "2: Soccer"
    elif b == 3:
        return "3: Volleyball"
    else:
        return "4: Ski"

temp = float(input('S\'il vous plait, mettre le temperature: '))
print(actTemp(temp))

########################### Excercise 3 #######################
print("************************** Excersise 3 *************************")

nombre = int(input("Un nombre entier: "))

def estDivisible (entier):
    if (entier%2 == 0 and entier%3 == 0):
        return 1;
    elif (entier%2 == 0 or entier%3 == 0):
        return 2;
    else:
        return 0;

print(estDivisible(nombre))

########################### Excercise 4 #######################
print("************************** Excersise 4 *************************")

a = float(input("Tapez le premier coefficient:"))
b = float(input("Tapez la deuxième coefficient:"))
c = float(input("Tapez la troisième coefficient:"))

def nombreRéel (x, y, z):
    if (y*y - 4*x*z) > 0:
        return 2;
    elif (y*y - 4*x*z) == 0:
        return 1;
    else:
        return 0;

print(nombreRéel(a,b,c))
