class Voiture:
    def __init__(self, marque = 'Ford', couleur = 'rouge'):
         self.marque = marque
         self.couleur = couleur
         self.pilote = 'personne'
         self.vitesse = 0

    def choix_conducteur(self, nom = ""):
        self.pilote = nom

    def accelerer (self, taux = 0.0, duree = 0.0):
        if self.pilote != 'personne':
            self.vitesse += taux*duree
        else:
            print("INACCESSIBLE")
    
    def affiche_tout (self):
        return self.marque + ' ' + self.couleur + ' pilotée par ' + self.pilote + ', vitesse = ' + str(self.vitesse)

    def __repr__ (self):
        return self.marque + ' ' + self.couleur + ' pilotée par ' + self.pilote + ', vitesse = ' + str(self.vitesse)
        
    def __eq__ (self, autre):
        return self.marque == autre.marque and self.couleur == autre.couleur and self.vitesse == autre.vitesse
        
