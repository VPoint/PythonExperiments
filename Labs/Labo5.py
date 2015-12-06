# Esther Raji
# Nombre d'étudiante: 8222130
# Labo #5

########################### Exercice 1: Calculer la moyenne ###############################
def moyenne(l):
    total = 0
    for x in l:
        total += float(x)
    
    return total/len(l)

liste = list(eval(input('Veuillez entrer une liste des nombres separees par virgules: ')))

print(moyenne(liste))

###################### Exercice 2: Le calcule de statistiques #############################
def notes(l):
    reponse = []
    total = 0
    ptt = float('inf')
    large = - float('inf')
    
    for i in l:
        if ptt > int(i):
            ptt = int(i)
        if large < int(i):
            large = int(i)
        total += float(i)

    reponse.append(total/len(l))
    reponse.append(ptt)
    reponse.append(large)
    
    return reponse

liste = list(eval(input('Veuillez entrer une liste des nombres separees par virgules: ')))

reponse = notes(liste)

print("Moyenne: ", reponse[0], "Minimum: ", reponse[1], "Maximum: ", reponse[2])

############################# Exercice 3: Lancer de balle #################################
import math

def lancer(v):
    distance = []

    for i in range(10):
        rad = i*10*(math.pi/180)
        val = (2*v*v*math.sin(rad)*math.cos(rad))/9.8
        distance.append("À " + str(i*10) + " degrées: " + str(val) + "m.")
    
    return distance

v = float(input("Entrer un velocité que tu aimerais calculer: "))
d = lancer(v)

for x in d:
    print(x)

################################# Exercice 4: Écart type ##################################
def écart(l):
    total = 0
    s2 = 0
    
    for x in l:
        total += float(x)

    a = total/len(l)

    for y in l:
        s2 += (float(y) - a)**2

    s = math.sqrt(s2/(
        len(l) - 1))
    
    return s

liste = list(eval(input('Veuillez entrer une liste des nombres separees par virgules: ')))

print("L'écart est ", écart(liste))
