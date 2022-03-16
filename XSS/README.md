# XSS Scanner

This script can be used in order to chek if a website
has reflected XSS vulnerability


## Install

```
pip install -r /path/to/requirements.txt
```

## Usage
```
#!/usr/bin/python3
from failleXSS.py import scan_xss

#url=input("Entrez l'url:") # URL input by user 
url="https://xss-game.appspot.com/level2/frame"
scan_xss(url)

```
<p align="center">
</p>

We have to input the url link, and the sentence send by the server when you uploaded an inccorrect file.




