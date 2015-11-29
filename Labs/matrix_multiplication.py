# Exercice 3: Multiplication de matrice
def produit_matrices(A,B):
    prod = [[]for i in A]
    
    x = 0
    while x < len(A):
        y = 0
        while y < len(B[0]):
            prod[x].append(A[x][0]*B[0][y])
            q = 1
            while q < len(A[0]):
                prod[x][y] += A[x][q]*B[q][y]
                q +=1
            y += 1
        x+= 1
    return prod

print('On veut multiplier deux matrices. Le premier DOIT avoir un nombre des colonnes égale au nombre des rangées du deuxième.')

L3=[[1,2,3],[4,5,6]]
L4=[[2,5],[3,6],[4,7]]

print('Ton premier matrice =', L3)
print('Ton deuxième matrice =', L4)

prodM = produit_matrices(L3,L4)
print(prodM)
