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

The script searches for forms in the given url and injects payloads in those forms until one works.

### Reflected Xss found
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/84924786/158654535-a0eac640-7e29-461a-9f81-18e4fd1f5f35.png">
</p>

### Reflected Xss not found
<p align="center">
  <img width="600" height="240" src="https://user-images.githubusercontent.com/84924786/158656160-bc55318d-a378-4241-a847-4f07c05b51a3.png">
</p>

```diff
! Warning : As you might see, Stored and DOM Based xss are not supported here.
```

