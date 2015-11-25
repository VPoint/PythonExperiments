class Temps:
  '''classe temporelle'''
  def __init__(self, h=12, m=0, s=0):
    '''(Temps)-> None'''
    self.setTemps(h,m,s)
    
  def setTemps(self, h, m=0, s=0):
    '''(Temps)-> None'''
    self.heure = h%24
    self.minute = m
    self.heure += m//60
    self.minute = m%60
    self.minute += s//60
    self.seconde = s%60

  def affiche_heure(self):
    '''(Temps)-> None'''
    print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))

  def estAvant(self, t2):
    '''retourne True si le temps représenté par self est avant le
    temps de t2, sinon elle retourne False.'''
    if self.heure < t2.heure:
      return True
    elif self.minute < t2.minute:
      return True
    elif self.seconde < t2.seconde:
      return True
    else:
      return False

  def durée(self, t2):
    '''retourne un nouvel objet Temps avec le nombre d’heures, de
    minutes, et de secondes entre self et t2.'''
    T3 = Temps()

    T3.heure = abs(self.heure - t2.heure)
    T3.minute = abs(self.minute - t2.minute)
    T3.seconde = abs(self.seconde - t2.seconde)
      
    return T3
    
  def __repr__(self):
    '''(Temps)-> str'''
    return (str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))

  def __eq__(self, autre):
    '''(Temps)-> bool'''
    return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde

