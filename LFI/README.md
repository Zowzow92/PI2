
# Local File Inclusion

This script can be used in order to check if there is a 
LFI vulnerability.



## Install

```
pip install -r /path/to/requirements.txt
```

## Usage
```
python3 LFI.py http://127.0.0.1/index.php?image={fuzz}
```
We have to input the url link and after the parameter add '{fuzz}'.
'{fuzz}' will be replace by payloads as '/etc/passwd'.

## Results
```
[+]SUCCESS - LFI vuln found with ../etc/passwd!"
```

