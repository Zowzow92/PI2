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

url=input("Entrez l'url:") # URL input by user 
#url="https://xss-game.appspot.com/level2/frame"
scan_xss(url)

```
<p align="center">
</p>

We have to input the url link.

## Result

<p align="center">
  <img width="400" height="240" src="![xss](https://user-images.githubusercontent.com/84924786/158654535-a0eac640-7e29-461a-9f81-18e4fd1f5f35.png)">
</p>

As we can see, the script searches for forms in the given url and injects payloads in those forms until one works.



