#!/usr/bin/python
import mechanize 
import itertools
import ssl
from bs4 import BeautifulSoup as btfs
import sys

class BT:
    '''
    Brute Force 
    
    Will test the target wesbite for Brute Force
     - Tests if the website block more than 3 attempts
     - Tests permutation password
     - Check response code HTTP
    
    Parameters:    
        URL of your target website
        Username Tag  
        Password Tag 
        
    Returns:
        
    '''
    def __init__(self):
        print("Veuillez saisir l'URL:")
        self.url = input();
        print("Saisir le tag du username:")
        self.usertag = input();
        print("Saisir le tage du password:")
        self.pwdtag = input()
        self.listpwd = itertools.permutations("i34U^hP-",8) 
    
    def SearchConsoleAdmin(self):
        '''
        Search for a console admin
        
        Returns:
                Suffix URL where an admin console is available
        '''
        pageSuffixe = ["/admin/","/administrator/","/admin.php","/wp-login.php",":21"];
        br = mechanize.Browser()
        exist = True
        for i in range(0,len(pageSuffixe)):
            exist = True
            try:
                
                self.url = self.url + "".join(pageSuffixe[i])
                
                reponse = br.open(self.url)
            except:
                print("Page "+ "".join(pageSuffixe[i]) + " inaccessible")
                exist = False
        
            if(exist == True):
                print("Page " + "".join(pageSuffixe[i]) +" accessible")
            
    
    def CheckReponse(self,txt):
        '''
        Check if a word is inside a source code of a website page 
         
        Parameters:    
            Server's request response
            
        Returns:
                True or False 
        '''
        # on Check si la contient un mot comme "incorrect", il faudrait une liste d'autres mots
        txt = btfs(txt,"lxml").get_text()
        txt= " ".join(item.strip().lower() for item in txt.split("\n")).split(" ")
        if("failed" in txt):
            #print("Failed auth")
            return True
        return False

    def Attack(self):
        '''
        Creates web browsing and finds if a
        LogIn form is secured or not
            
        Returns:
                Print out success or errors
        '''
        ssl._create_default_https_context = ssl._create_unverified_context
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        compteur = 0
        combos= self.listpwd 
        try:
            reponse = br.open(self.url)
        except :
            print("Url introuvable")
            sys.exit()

        try:
            for x in combos:
                br.set_response(reponse)
                try:
                    br.select_form( nr = 0 )
                    br.form[self.usertag] = "user name"
                    br.form[self.pwdtag] = ''.join(x)
                    print("Checking user:",br.form[self.usertag]," password:",br.form[self.pwdtag])
                except :
                    print("Formulaire introuvable")
                    break
                reponse = br.submit()
                # if(self.CheckReponse(reponse.read())):
                # print("Incorrect")
                print("Code reponse HTTP",reponse.code)
                if(reponse.code/100>=5):
                    print("Erreur client")
                elif(reponse.code/100>=4):
                    print("Erreur Serveur")
                    break
                elif(reponse.code/100>=2 and reponse.code/100<=3):
                    print("Succes")
                        
                compteur+=1
                if(compteur == 4):
                    break
        except :
            print("Site sécurisé")


end = ""
while(end != "quit"):
    
    b = BT()
    b.Attack()
    b.SearchConsoleAdmin()
    end = input("Write quit if you want to end the program : ")
