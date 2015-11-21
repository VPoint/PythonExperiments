from math import sqrt
#################### Excercise 1 ##########################
print ("*************Division des entiers*************")
x = int(input("Taper un nombre: "))
y = int(input("Et un autre: "))

print("Le division de", x, "par", y, "est", x//y, "avec", x%y,"qui reste.")

#################### Excercise 2 ##########################
print ("*************Changer le temperature*************")
celsius = float(input("Mettre un temperature en celsius: "))

def deCenF(cel):
    far = (cel)*9.0/5.0 + 32
    return far

farenheit = deCenF(celsius)

print(celsius, "celsius egal", farenheit,"farenheit.")

#################### Excercise 3 ##########################
print ("*************Calculer ton note*************")
devoirsMoyenne = float(input("Devoirs: "))
partiel = float(input("Partiel: "))
examen = float(input("Examen: "))

def calculNote(devoir, part, exam):
    note = devoir*(25.0/100.0) + part*(25.0/100.0) + exam*(50.0/100.0)
    return note

print ("Note: " + str(calculNote(devoirsMoyenne, partiel, examen)))

#################### Excercise 4 ##########################
print ("*************Calculer la surface d'un triangle*************")
côté_1 = float(input("Côté 1: "))
côté_2 = float(input("Côté 2: "))
côté_3 = float(input("Côté 3: "))

def calculeSurface(A, B, C):
    p = A + B + C
    s = sqrt(p*(p-2*A)*(p-2*B)*(p-2*C))/4
    return s

aire = calculeSurface(côté_1,côté_2,côté_3)

print("Aire: " + str(aire))
