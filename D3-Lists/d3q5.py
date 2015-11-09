# Cette programme prends les résultats d'un vote comme données et retourne le résultat:
# unanimité, majorité claire, majorité simple, la motion ne passe pas. Un fonction est
# utiliser pour calculer le pourcentage et les conditions détermine la résultat.

def vote_pourcentage(ch):
    ''' paramètres (un chaîne des charactère) et retourne un float

    Cet fonction utilise les modules définies dans la documentation pour les chaînes
    des charactères pour conter le nombre des oui ou non. Utilisant cette information,
    Il est alors possible à calculer le pourcentage des voteurs actives qui pense que
    la motion devrait passer. La fonction retourne cette pourcentage. Les abstentions
    ne sont pas calculées. '''

    # La programme conte le nombre des 'oui''s et des 'non''s
    nOui = float(ch.count('oui'))
    nNon = float(ch.count('non'))

    # On calcule le pourcentage des oui de toutes les gens qui on voté oui, ou non
    pourcentage = nOui/(nOui+nNon)
    return pourcentage
        
# Ici, la program demande l'utilisateur pour les resultats du vote
votes = input('''Entrez les votes (oui, non, ou abstention) séparés par des espaces, et à la
          fin appuyez enter: ''')

# La fonction est appèlé
p = vote_pourcentage(votes)

# On compare la pourcentage calculé avec les définitions pour déterminer si la motion est
# passé.
if(p == 1):
    print('unanimité')
elif (p >= 2/3):
    print('majorité claire')
elif (p >= 1/2):
    print('majorité simple')
else:
    print('la motion ne passe pas')
