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

def lineaire(l, v):
    NPas = 0
    for x in l:
        NPas += 1
        if x == v:
            print ("Nombre de pas:", NPas)
            return True
    print ("Nombre de pas:", NPas)
    return False

print (lineaire(l3, v))

def cherche_m(m, v):
    NPas = 0
    for x in m:
        for y in x:
            NPas += 1
            if y == v:
                print ("Nombre de pas:", NPas)
                return True
    print ("Nombre de pas:", NPas)
    return False

print(cherche_m(M, v))

l3.sort()

def recherche_binaire(L, v):
  """ (list, int) -> int
  Retourne la position de v dans la liste trie L,
  ou -1 si v n’est pas dans L.
  >>> recherche_binaire([1, 3, 4, 4, 5, 7, 9, 10], 10)
  7
  >>> recherche_binaire([1, 3, 4, 4, 5, 7, 9, 10], -3)
  -1
  >>> recherche_binaire([], -3)
  -1
  >>> recherche_binaire([1], 1)
  0
  """
  position = -1
  # i et j delimitent la section de recherche
  i = 0
  j = len(L) - 1
  NPas = 0
  while i != j + 1:
    NPas += 1
    m = (i + j) // 2  # trouve le milieu
    if L[m] == v:   # si on a trouve, retourne la position
      print ('Nombre des pas:', NPas)
      return True
      break
    elif L[m] < v:  # fouille a la droite 
      i = m + 1
    else:           # fouille a la gauche
      j = m - 1
      
  print ('Nombre des pas:', NPas)
  return False

print(recherche_binaire(l3, v))
##NPas = 0
##def binaire(l, r, commence, termine):
##    loc = commence + ((termine-1) - commence)//2
##    global NPas
##    if ((termine-1) - commence) < 1 and loc != r:
##        print(False)
##    else:
##        if l[loc] < r:
##            NPas += 1
##            binaire(l, r, loc+1, termine)
##        elif l[loc] > r:
##            NPas += 1
##            binaire(l, r, commence, loc-1)
##        else:
##            NPas += 1
##            print(True)
##
##print(binaire(l3, v, 0, len(l3)))
##print ("Nombre de pas:", NPas)
