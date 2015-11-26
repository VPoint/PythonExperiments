import turtle
# La bibliotèque utilisé dans cette jeu varie car les images sont des triangles
# et cercles au lieu des 'X' et des 'O'
import d4q3Lib_TC

print(''' Pour jouer, cliquez sur la position que tu veux bouger l'objet
 deux fois, le premier pour la locatoin et la deuxième fois sur l'objet.
 Dans cette jeu, les trianges représent les X et les cercles représent les O.
 Tu peux pas jouer dans le cercle pour le premier tourne car les objects
 commence dans le centre. ''')

# Définir le tableau
screen = turtle.Screen()
screen.title("Tic-Tac-Toe!!")
screen.bgpic("board.gif")

# Créer un objet pour representer 'O', dans ce cas un cercle
O = turtle.Turtle()
O.shapesize(9, 9, 1)
O.shape('circle')
O.fillcolor('green')

# Créer un objet pour representer 'X', dans ce cas un triangle
X = turtle.Turtle()
X.shapesize(9, 9, 1)
X.shape('triangle')
X.fillcolor('red')

# Enlève les lignes de tracer les movements de chaque objet
O.up()
X.up()

# cette variable verifie que les objets pouvait seulement bouger lorsque
# c'est son tourne
turn = True

# cette fonction bouge l'objet O ou l'usager a cliqué
def moveO(x,y):
    global turn
    if not turn:
        O.goto(x, y)
        # emprime les nouvelle coordonées de O
        print('O =',O.pos())
        turn = True

# cette fonction bouge l'objet X ou l'usager a cliqué
def moveX(x,y):
    global turn
    if turn:
        X.goto(x, y)
        # emprime les nouvelle coordonées de X
        print('X =',X.pos())
        turn = False

# Ici, on creait un tableau pour utiliser les fonctions avec
tableau = [['-','-','-'],['-','-','-'],['-','-','-']]

def verifie(p,q, n):
    '''On utilise verifie pour verifier si la position est remplit
       En Python, cette fonction place les objets dans le tableau.
       Il peut verifier si la position est remplit, MAIS il ne peut pas forcer
       l'usager à changer leur position. Il ne place pas un image sur un
       position remplit, alors L'usager peut changer leur position dans leur
       prochaine tourne.'''
    if tableau[p][q] == '-':
          # place un image de l'objet sur la position
          n.stamp()
          
          # placer l'objet dans le tableau
          tableau[p][q] = str(n.shape())
          print("Tableau [",p,"][",q,"]: ", n.shape())

def enListe(n):
    '''Cette fonction accepte des objects et retourne rien.
    Il est chargé d'utiliser les co-ordonnées pour remplire le tableau.
    Pour chaque coordoné de l'objet, il appelle la fonction verifie et place
    un image sur la position de l'objet.'''
    global done
    if(n.xcor() < -100.00):
        if (n.ycor() > 100.00):
            verifie(0,0, n)
        elif (n.ycor() > -100.00 and n.ycor() < 100.00):
            verifie(1,0, n)
        elif (n.ycor() < - 100.00):
            verifie(2,0, n)
    elif(n.xcor() > -100.00 and n.xcor() < 100.00):
        if (n.ycor() > 100.00):
            verifie(0,1, n)
        elif (n.ycor() > -100.00 and n.ycor() < 100.00) and done > 2:
            verifie(1,1, n)
        elif (n.ycor() < -100.00):
            verifie(2,1, n)
    elif(n.xcor() > 100.00):
        if (n.ycor() > 100.00):
            verifie(0,2, n)
        elif (n.ycor() > -100.00 and n.ycor() < 100.00):
            verifie(1,2, n)
        elif (n.ycor() < -100.00):
            verifie(2,2, n)
    else:
        print("SVP choisir un des places dans le tableau.")

# le variable done est pour verifier le tourne
done = 0
# le variable gagnant varifie si quelqu'un a gagné
gagnant = False

def doneGame(x,y):
    print('DONE PLUS ONE')
    global done
    done += 1

# Lorsqu'il n'y a pas de gagnant et le tableau n'est pas remplit, le boucle continue
while not gagnant and not d4q3Lib_TC.testMatchNul(tableau):
    if(done%2==0):
        # Pour les changements paires dans le jeu, 'X' ou le triangle bouge
        # Quand l'écran est cliqué, bouge l'object X à la position
        screen.onclick(moveX)

        # Quand On clique X un deuxième fois, la tourne est terminé
        X.onrelease(doneGame)

        # On ajoute l'objet dans la liste
        enListe(X)
        
        # verifier si'il y a un gagnant, si non, continuer la boucle
        gagnant = d4q3Lib_TC.verifieGagner(tableau)
    else:
        # Pour les changements impaires dans le jeu, 'O' ou le cercle bouge
        screen.onclick(moveO)

        # Quand On clique O un deuxième fois, la tourne est terminé
        O.onrelease(doneGame)

        # On ajoute l'objet dans la liste
        enListe(O)
        
        # verifier si'il y a un gagnant, si non, continuer la boucle
        gagnant = d4q3Lib_TC.verifieGagner(tableau)

# Enlever la function pour changer la position des objects sur l'écran
screen.onclick(None)
print('Game Over!!')

# Emprime le tableau gagnant
for l in tableau:
    print (l)

        
