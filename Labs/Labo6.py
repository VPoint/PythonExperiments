########################### Exercice 1 ###############################
s1 = 'bon'
s2 = 'mauvais'
s3 = 'fou'

print('ou' in s3) # a)
print(' ' not in s1) # b)
print(s1 + s2 + s3) # c)
print(s1 + ' ' + s2 + ' ' + s3) # d)
print(s3*10) # e)
print(len(s1 + s2 + s3)) # f)

########################### Exercice 2 ###############################
aha = 'abcdefgh'

print(aha[:4]) # a)
print(aha[3:6]) # b)
print(aha[7]) # c)
print(aha[5:7]) # d)
print(aha[3:]) # e)
print(aha[5:]) # f)
print(aha[0]+aha[3]+aha[6]) # g)
print(aha[-7]+aha[-5]) # h)

########################### Exercice 3 ###############################
s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''


nS = s.replace('.',' ').replace(',',' ').replace(';',' ').replace('\n',' ')
nS = nS.strip()
nS = nS.lower()
num = nS.count('de')
nS = nS.replace('était','est')

print(nS)

########################### Exercice 4 ###############################
def compte(s,c):
    return s.count(c)

def compte2 (s,c):
    s = s.lower()
    num = 0
    i = 0
    while (i < len(s)) and (i+len(c)):
        if (s[i:(i+len(c))]) == c:
            num += 1
        i += 1

    return num

s = input('Tapez quelque chose: ')

print(compte2(s,'de la'))
print(compte2(s,'a'))

print(compte(s,'de la'))
print(compte(s,'a'))

########################### Exercice 5 ###############################
def espaces(s):
    return s.replace('', ' ')

s = input('Tapez quelque chose: ')
print(espaces(s))

########################### Exercice 6 ###############################
def coder(s):
    newS = ''
    if not(len(s)%2 == 0):
        s = s + ' '
    
    for x in range(1, len(s), 2):
        newS += s[x] + s[x-1]
    
    return newS

s = input('Tapez quelque chose: ')
print(coder(s))
























