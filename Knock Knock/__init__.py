import os
import LFI.py 
import BruteForce.py
import FailleXSS.py


def AffichageMenu():
    print('Selectionnez un scan :\n'
          '\t[1] XSS\n'
          '\t[2] Brute Force\n'
          '\t[3] Faille d\'Upload\n'
          '\t[4] Local File Inclusion\n'
          '\t[5] Quitter\n')

def AffichageBruteForce():
    b = BruteForce.BT()
    b.Attack()
    b.SearchConsoleAdmin()

def AffichageXSS():
    url=input("Entrez l'url:") 
    FailleXSS.scan_xss(url)

def AffichageLFI():
    LFI.LFI()

def selectScan(slct):
    
    pass    
    
slct = -1
fin = 0
while fin == 0:
    os.system('cls')
    AffichageMenu()
    try:
        slct = int(input())
    except ValueError :
        print("Saisir une valeur entre 1 et 5")
    if(slct == 1):
        AffichageXSS()
    if(slct == 2):
        AffichageBruteForce()
    if(slct == 3):
        AffichageBruteForce()
    if(slct == 4):
        AffichageLFI()
    if(slct == 5):
        fin = 1
