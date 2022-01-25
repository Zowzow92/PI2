
# Brute Force

This script can be used in order to chek if a website
has a secured Login and if a console is available.

## Usage
```
#!/usr/bin/python3
from BruteForceFinalVersion.py import BT

bruteforce = BT()
bruteforce.Attack() // To check security Login
bruteforce.SearchConsoleAdmin() // To find any admin console available

```
<p align="center">
  <img width="200" height="150" src="https://user-images.githubusercontent.com/58170434/150952341-a9762451-7987-4853-a1b7-268c480140b6.jpg">
</p>

We have to input the url link, the username tag of the login form (use dev tool of your browser) and 
the password tag.

## Results

### Attack
<p align="center">
  <img width="400" height="240" src="https://user-images.githubusercontent.com/58170434/150953724-262cea46-0ff6-4c8d-8827-2d03c5788b36.jpg">
</p>

As we see the script tried credentials until the form disabled, wich means that the login form is secrured against BruteFroce attacks.

### SearchConsoleAdmin

<p align="center">
  <img width="300" height="140" src="https://user-images.githubusercontent.com/58170434/150955155-5567eead-8a90-44b0-b849-db4f6eb275cf.jpg">
</p>

The script returns all admin paths that are not blocked.


