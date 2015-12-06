# Exercice 1

def histo(ch):
    histogramme = {}
    for x in ch:
        histogramme[x] = histogramme.get(x, 0) + 1
    return histogramme

s = input('Entrer un chaîne des charactères:')
alphdict = list(histo(s).items())
alphdict.sort()
print(alphdict)

# Exercice 2

def histo_t(t):
    '''(tuple)->dict
    Retourne un dictionnaire
    Precondition: le tuple contient des entiers
    >>> t = (1,2,-3,3,4,-3,3,3)
    >>> histo_n(t)
    {1: 1, 2: 1, 3: 3, 4: 1, -3: 2}
    '''
    histogramme = {}
    for x in t:
        histogramme[x] = histogramme.get(x, 0) + 1
    return histogramme

tup = tuple(eval(input('Entrer une tuple séparés par des virgules:')))
print(tup)
numdict = list(histo_t(tup).items())
numdict.sort()
print(numdict)

# Exercice 3

def somme_de_trois(x):
     '''(tuple)->bool
     Retourne True si la somme de 3 elements
     consecutive est zero
     Precondition: le tuple a au moins 3
     elements
     >>> t = (1,2,-3,4,-1,3)
     >>> somme_de_trois(t)
     True '''
     i = 0
     while i < (len(x)-2):
         if(x[i]+ x[i+1]+ x[i+2]) == 0:
            return True
         i += 1
     return False

tup = tuple(eval(input('Entrer une tuple séparés par des virgules:')))
print (somme_de_trois(tup))

# Exercice 4
def move_zeros_v1(l):
    tmp = []
    for x in l:
        if x != 0:
            tmp.append(x)
    while len(tmp) < len(l):
        tmp.append(0)
    return tmp
    
def move_zeros_v2(l):
    longeur = len(l)
    tmp = []
    for x in l:
        if x != 0:
            tmp.append(x)
        
    while len(tmp) < longeur:
        tmp.append(0)
    del l[:]

    for y in tmp:
        l.append(y)

def move_zeros_v3(l):
    i = 0
    for n in l:
        if n != 0:
            x = n
            index = l.index(x, i)
            for y in range(0, index):
                if l[y] == 0:
                    l[index] = 0
                    l[y] = x
                    break;
        i += 1

# Version 1
liste = list(eval(input("Entrer un liste separe par des virgules: ")))

x = move_zeros_v1(liste)
print(liste, x)

# Version 2
liste = list(eval(input("Entrer un liste separe par des virgules: ")))

y = move_zeros_v2(liste)
print(liste, y)

# Version 3
liste = list(eval(input("Entrer un liste separe par des virgules: ")))

z = move_zeros_v3(liste)

print(liste, z)
