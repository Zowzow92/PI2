import os

def AffichageMenu():
    print('Selectionnez un scan :\n'
          '\t[1] XSS\n'
          '\t[2] Brute Force\n'
          '\t[3] Faille d\'Upload\n'
          '\t[4] Local File Inclusion\n'
          '\t[5] Quitter\n')

def selectScan(slct):
    
    pass    
    
slct = -1
while slct == -1:
    os.system('cls')
    AffichageMenu()
    try:
        slct = int(input())
    except ValueError :
        print("Saisir une valeur entre 1 et 5")
