from random import shuffle

class Blackjack:
 valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
 def joue(self):
  '''jour un jeu'''   
  d = JeuDeCartes()
  d.battre()
  
  banque = Main('Banque')
  joueur = Main('Joueur')

  # donne deux cartes au joueur et deux cartes a la banque
  for i in range(2):  
    joueur.ajouteCarte(d.tireCarte())
    banque.ajouteCarte(d.tireCarte())

  # montre les mains
  banque.montreMain()
  joueur.montreMain()

  # tant que le joueur demande Carte!, la banque tire des cartes
  reponse = input('Carte? Oui ou non? (Par défaut oui) ')
  while reponse in ['','o','O','oui','Oui']:
    c = d.tireCarte()
    print("Vous avez:")
    print(c)
    joueur.ajouteCarte(c)
    if self.total(joueur) > 21:
       print("Vous avez dépassé 21. Vous avez perdu.")
       return   
    reponse = input('Carte? Oui ou non? (Par défaut oui) ')

  # la banque joue avec ses regles  
  while self.total(banque) < 17:
    c = d.tireCarte()
    print("La banque a:")
    print(c)
    banque.ajouteCarte(c)
    if self.total(banque) > 21:
       print("La banque a dépassé 21. Vous avez gagné.")
       return

  # si 21 n'est pas depassée, compare les mains pour trouver le gagnat  
  self.compare(banque, joueur)

      
 def total(self, main):
    ''' (Main) -> int
    calcule la somme des valeur de toutes les cartes dans la main
    '''
    somme = 0;
    numA = 0
    # a completer
    
    for k in main.main:# calculez la somme de toutes les valeurs de la main
        j = k.valeur
        if j == '2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9':
            somme += int(j)
        elif j == 'J'or j=='Q' or j=='K' or j=='10':
            somme += 10
        else:
            numA += 1
            somme += 11
    if somme > 21: # while la somme > 21 et il y a des As, deduisez 10 points pour chaque As
        while numA > 0:
            somme -= 10
            if somme == 21 or somme < 21:
                break;
            else:
                numA -= 1

    return somme # a changer

 def compare(self, banque, joueur):
    ''' (Main, Main) -> bool
    Compare la main du joueur avec la main de la banque
    et affiche de messages
    '''

    # a completer

    b = self.total(banque)# applelez la methode self.total pour la banque et pour le joueur
    j = self.total(joueur)
    # si le total de la banque > le total du joueur affichez 'Vous avez perdu.'
    if b > j:
        print('Vous avez perdu.')
    # si le total de la banque < le total du joueur affichez 'Vous avez gagné.'   
    elif b < j:
        print('Vous avez gagné.')
    # en cas d'egalite, si le total est 21m si la banque a un blackjack
    # affichez 'Vous avez perdu.'; si le joueur a un blackjack 'Vous avez gagné.' 
    # sinon, affichez 'Egalité.'

       
class Main(object):
    '''represente une main des cartes a jouer'''

    def __init__(self, joueur):
        '''(Main, str)-> none
        initialise le nom du joueur et la liste de cartes avec liste vide'''
        
        self.nom = joueur
        self.main = [] # a completer

    def ajouteCarte(self, carte):
        '''(Main, Carte) -> None
        ajoute une carte a la main'''
        
        self.main.append(carte)# a completer

    def montreMain(self):
        '''(Main)-> None
        affiche le nom du joueur et la main'''

        print(self.nom, 'a dans sa main: ', self.main)# a completer
                
    def __eq__(self, autre):
        '''retourne True si les main ont les meme cartes
           dans la meme ordre'''
        if len(self.main) > len(autre.main) or len(self.main) < len(autre.main):
            return False

        for x in range(len(self.main)):
            comp = self.main[x] == autre.main[x]
            if not comp:
                break; # a completer
        return comp

    def __repr__(self):
        '''retourne une representation de l'objet'''
        # 'La main du joueur ' + self.nom + ' est ' + 
        return self.main
        # a completer

class Carte:
    '''represente une carte a jouer'''

    def __init__(self, valeur, couleur):
        '''(Carte,str,str)->None        
        initialise la valeur et la couleur de la carte'''
        self.valeur = valeur
        self.couleur = couleur  # pique, coeur, trefle ou carreau

    def __repr__(self):
        '''(Carte)->str
        retourne une representation de l'objet'''
        return 'Carte('+self.valeur+', '+self.couleur+')'

    def __eq__(self, autre):
        '''(Carte,Carte)->bool
        self == autre si la valeur et la couleur sont les memes'''
        return self.valeur == autre.valeur and self.couleur == autre.couleur

class JeuDeCartes:
    '''represente une jeu de 52 cartes'''
    # valeurs et couleurs sont des variables de classe
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    # couleurs est un set de 4 symboles Unicode qui representent les 4 couleurs
    # pique, coeur, trefle ou carreau
    
    def __init__(self):
        'initialise le paquet de 52 cartes'
        self.paquet = []          # paquet vide au debut
        for couleur in JeuDeCartes.couleurs: 
            for valeur in JeuDeCartes.valeurs: # variables de classe
                # ajoute une Carte de valeur et couleur
                self.paquet.append(Carte(valeur,couleur))

    def tireCarte(self):
        '''(JeuDeCartes)->Carte
        distribue une carte, la premiere du paquet'''
        return self.paquet.pop()

    def battre(self):
        '''(JeuDeCartes)->None
        pour battre le jeu des cartes'''
        shuffle(self.paquet)

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return 'Paquet('+str(self.paquet)+')'

    def __eq__(self, autre):
        '''retourne True si les paquets ont les meme cartes
           dans la meme ordre'''
        return self.paquet == autre.paquet
    
    
b = Blackjack()
b.joue()

