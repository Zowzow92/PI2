import os
import LFI.py 
import BruteForce.py
import FailleXSS.py
import fuxploider.py


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
  
def Fuxploider():
    print("Sasir l'url:")
    url = input()
    #[!] Attention - Si tout les types de fichiers sont testés et valide, c'est certainement que le not-regex qui a mal été saisit
    print("Type the \'not-regex\' (Exemple: \"wrong file type\") Attention à bien le message d'erreur saisir"
    nregex = input()
    cmd = 'python3 fuxploider.py --url {} --not-regex \"{}\"'.format(url,nregex)
    os.system(cmd)

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
        Fuxploider()
    if(slct == 4):
        AffichageLFI()
    if(slct == 5):
        fin = 1
