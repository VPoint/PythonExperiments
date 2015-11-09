# Cette program affiche les entiers de a à b, incluant a et b

def conter(x, y):
    'Cette fonction affiche les entiers de x à y, incluant x et y'
    for n in range (x, y + 1):
        # Cette boucle incrément chaque valeur
        print(n)

# L'usager entre les deux entiers du clavier
a = int(input('SVP donner la valeur de a: '))
b = int(input('SVP donner la valeur de b: '))

# Un appelle au fonction
conter(a,b)
