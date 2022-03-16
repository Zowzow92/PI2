# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 12:41:32 2021

@author: fdial
"""
import requests
from tqdm import tqdm
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from termcolor import colored



"""
Given an url, it returns all forms from the HTML content
"""
def get_all_forms(url):
    
    """" get the page source code"""
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

############################################################################

"""
return all information about the Html form
"""
def get_form_details(form):
   
    details = {}
    # get the form action (target url/redirection url)
    details["action"] = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc.)
    details["method"] = form.attrs.get("method", "get").lower() 
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["inputs"] = inputs
    return details

############################################################################

"""
    Submits a form given in "get_form_details()"
    Params:
        form_details (list): a dictionary that contain form information
        url (str): the original URL that contain that form
        value (str): the script we want to execute
    Returns the HTTP Response after form submission
"""
def submit_form(form_details, url, value):
    
    # construct the full URL (if the url provided in action is relative)
    target_url = urljoin(url, form_details["action"])
    # get the inputs
    inputs = form_details["inputs"]
    data = {}
    for input_tag in inputs:
        # replace all text and search values with "value"
        if input_tag["type"] == "text" or input_tag["type"] == "search":
            input_tag["value"] = value
        input_name = input_tag.get("name")
        input_value = input_tag.get("value")
        if input_name and input_value:
            # if input name and value are not None, 
            # then add them to the data of form submission
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)

############################################################################

"""
    Given an url, it prints all the vulnerable forms founded
"""
def scan_xss(url):
    
    is_vulnerable=False
    payloadLength=len(open('xssPayload.txt','r',encoding="utf-8").readlines())
    
    # get all the forms from the URL
    forms = get_all_forms(url)
    print(colored("\n[WARNING ]","cyan")," Detected ",len(forms)," forms on ",url)
    
    # iterate over all forms
    for form in forms:
        
        with open('xssPayload.txt',encoding="utf-8") as f:
            
            for script in tqdm(f,total=payloadLength,colour="green",desc="Scanning"):
                
                form_details = get_form_details(form)
                #get the HTTP Response after form submission
                content = submit_form(form_details, url, script).content.decode()
                if script in content:
                    print(colored("\n[CRITICAL]","red"), " Reflected XSS found")
                    print(colored("[  INFO  ]","green")," Form details:")
                    pprint(form_details)
                    is_vulnerable=True
                    break #because if one work it will mean that there is a xss breach so we don't
                          #have to continue testing the other scripts
                          
    if not is_vulnerable:
        print(colored("\nXSS vulnerability not found","green"))
    
    return is_vulnerable


####################################TEST########################################
if __name__ == "__main__":
    #url=input("Entrez l'url:") 
    url="https://xss-game.appspot.com/level2/frame"
    scan_xss(url)
