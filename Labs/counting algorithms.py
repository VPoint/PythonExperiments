import random

N = 10
l3 = []
for i in range(N):
    v = random.randrange(1,N+1)
    l3.append(v)
print('Liste: ', l3)

M = []
for i in range(10):
    M.append([])
    for j in range(10):
        v = random.randrange(1,N+1)
        M[i].append(v)
print('Matrice :')
for x in M:
    print(x)

v = int(input('Tapez un nombre pour chercher la liste et la matrice: '))

def compte(l, v):
    num = 0
    NPas = 0
    for x in l:
        NPas += 1
        if x == v:
            num += 1
    print ("Nombre de pas", NPas)
    
    return num

print (compte(l3, v))

def compte_m(m,v):
    num = 0
    NPas = 0
    for x in m:
        for y in x:
            NPas += 1
            if y == v:
                num += 1
    print ("Nombre de pas", NPas)
    return num

print(compte_m(M, v))
