def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   i = 0 #i représente les rangées
   j = 0 #j représente les colonnes

   while i <=2: #puisque c'est un jeu de tic-tac-toe, la matrice est limité
       j=0
       while j<= 2:
        
           tab[i][j] = "-" #ajoute le caractère - pour signaler qu'il n'y a rien 

           j+=1
       i+=1
        
       # retourne rien

def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    choix = testCols(tab)
    if choix == "X" or choix == "O": #Vérifie si une colonne gagne
       print("Le joueur " + choix + " a gagné!")
       return True
    choix = testLignes(tab)
    if choix == "X" or choix == "O": #Vérifie si une ligne gagne
       print("Le joueur " + choix + " a gagné!")
       return True
    choix = testDiags(tab)
    if choix == "X" or choix == "O": #Vérifie si une diagonale gagne
       print("Le joueur " + choix + " a gagné!")
       return True

    if testMatchNul(tab) == True: #Vérifie si le jeu peut encore continué
       print("Match nul!")
       return True
    
   
    return False  # quelqu'un peut encore gagner

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   réponse = "-" #initialise réponse
   i = 0 # i représente les rangées
   while i <= 2: #puisque c'est un jeu de tic-tac-toe, la matrice est limité
      j = 0
      while j <=2: # j représente les colonnes
         choix = tab[i][0] #prend le premier élément de la ligne
         if choix == tab[i][1] and choix == tab[i][2] and (choix == "X" or choix == "O"): #est-ce que cet élément est identique aux deux autres de cette ligne?
            réponse = choix #choix se trouve dans les 2 éléments de la ligne
            
            break
         j = j + 1
      i = i + 1
  
   return réponse 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   réponse = "-" # initilialise réponse et j
   j = 0
   while j <=2: # j représente les colonnes
      
      choix = tab[0][j]# prend la valeur de la première colonne
      if choix == tab[1][j] and choix == tab[2][j] and (choix == "X" or choix == "O"): #est-ce que cet élément est identique aux deux autres de cette colonnes?
         réponse = choix #le choix se retrouve dans les deux autres colonnes
         
         break
      j = j + 1
  
   return réponse

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   réponse = "-"
   #Vérifie première diagonale pour X
   if tab[0][0] == "X" and tab[1][1] == "X" and tab[2][2] == "X":
      réponse = "X"
      
   #Vérifie deuxième diagonale pour X
   if tab[0][2] == "X" and tab[1][1] == "X" and tab[2][0] == "X":
      réponse = "X"
      
   #Vérifie première diagonale pour X
   if tab[0][0] == "O" and tab[1][1] == "O" and tab[2][2] == "O":
      réponse = "O"
      
   #Vérifie deuxième diagonale pour O
   if tab[0][2] == "O" and tab[1][1] == "O" and tab[2][0] == "O":
      réponse = "O"
      
    
   return réponse

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   i = 0 # i représente les rangées
   compteur = 0 #compte le nombre de "X" ou de "O" sont présent dans la matrice
   while i <= 2: # jeu de tic-tac-toe donc la matrice est fixe
      j = 0 # j représente les colonnes
      while j <= 2:
         if tab[i][j] != "-" : # si la boucle détecte une matrice pleine, les autres tests ont vérifier qu'il n'y avait aucune victoire
            compteur = compteur + 1
            
         j = j + 1
      i = i + 1

   if compteur == 9: #est-ce qu'il y a une matrice pleine, donc 9 cases remplit?
      return True
   return False
  

