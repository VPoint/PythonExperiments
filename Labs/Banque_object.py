class CompteBancaire(object):
    def __init__(self, nom = 'Dupont', solde = 1000):
        self.nom = nom
        self.solde = solde
        
    def depot(self, somme = 0):
        self.solde += somme

    def retrait(self, somme = 0):
        self.solde -= somme

    def affiche(self):
        return self.nom + ' possede ' + str(self.solde) +' dans son compte.'
    def __eq__(self, autre):
        return self.solde == self.solde
    
    def __repr__(self):
        return 'Nom: ' + self.nom + ', Solde: ' + str(self.solde)
class CompteEpargne(CompteBancaire):
    def __init__(self, nom = 'Dupont', solde = 1000):
           CompteBancaire.__init__(self, nom, solde)
           self.taux = 0.003
       
    def changeTaux(self, valeur = 1):
           self.taux = valeur
           
    def capitalisation(self, nombreMois = 0):
           print('Nombre des mois: ', nombreMois)
           print('Taux de capitalisation: ', self.taux)
           self.solde += (self.solde*self.taux)*nombreMois
           print('Total: ', self.solde)

        
