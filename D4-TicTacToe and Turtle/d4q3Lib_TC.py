def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   i = 0
   j = 0

   while i <=2:
       j=0
       while j<= 2:
        
           tab[i][j] = "-"

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

    if testCols(tab) or testLignes(tab) or testDiags(tab):
       return True #quelqu'un a gagné
    elif testMatchNul(tab):
       return True #il est encore possible de gagné
    else:
       return False

 
def testLignes(tab):
   ''' (list) ->  bool
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   i = 0
   while i <= 2:
         choix = tab[i][0] #prend le premier élément de la ligne
         if choix == tab[i][1] and choix == tab[i][2]: #est-ce que cet élément est identique aux deux autres de cette ligne?
            if choix == "triangle" or choix == "circle": #est-ce que réponse est un X ou un O, il est possible que c'est -
                  print("Joueur " + choix + " a gagné!") #choix se trouve dans les 2 éléments de la ligne
                  print("LIGNE")
                  return True # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant
            else:
               return False
         i = i + 1
  
  
def testCols(tab):
   ''' (list) ->  bool
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   i = 0
   
   while i <= 2:
      choix = tab[0][i]
      if choix == tab[1][i] and choix == tab[2][i]:
            if choix == "triangle" or choix == "circle":
               print("Joueur " + choix + " a gagné!")
               print("COLUMN")
               return True
            else:
               return False

      i = i + 1
             
   #a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

   
def testDiags(tab):
   ''' (list) ->  bool
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   choix = tab[0][0]
   #Vérifie première diagonale pour le choix
   if tab[1][1] == choix and tab[2][2] == choix:
      if choix == "triangle" or choix == "circle": #est-ce que réponse est un X ou un O, il est possible que c'est -
         print("Joueur " + choix + " a gagné!") #choix se trouve dans les 2 éléments de la ligne
         print("DIAGONAL 1")
         return True # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant
   #Vérifie deuxième diagonale pour le choix
   else:
      choix = tab[0][2]
      if tab[1][1] == choix and tab[2][0] == choix:
         if choix == "triangle" or choix == "circle": #est-ce que réponse est un X ou un O, il est possible que c'est -
             print("Joueur " + choix + " a gagné!") #choix se trouve dans les 2 éléments de la ligne
             print("DIAGONAL 2")
             return True # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant
      else:
         return False
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   i = 0
   while i <= 2:
      j = 0
      while j <= 2:
         if tab[i][j] == "-": # si la boucle détecte un seul - elle s'arrête et retourn False
            return False
         j = j + 1
      i = i + 1
   print('Tableau Remplit.')
   return True
  
   
