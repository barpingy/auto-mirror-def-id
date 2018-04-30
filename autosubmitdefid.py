# -*- coding: UTF8 -*-

# Thx To Stack Overflow For Bypass DDoS Protection

try:
	import cfscrape
	import re
	import sys
	import time
except Exception as ez:
	print("\033[31;1m[ERROR]\033[0m "+str(ez))
	exit()

def help():
	print("\n\n\033[32;1m[\033[0mDefacerID Mass Notifier\033[32;1m]\033[0m\n\033[32;1m[\033[0mRUN\033[32;1m]\033[0m python DefacerID.py list.txt\n\n")
	sys.exit()

try:
	listerhek = sys.argv[1]
except:
	help()
	sys.exit()

Kwontolz = "https://defacer.id/archives/notify"
Mr.BrPinG = cfscrape.create_scraper()
heker = "Mr.BrPinG"
tim = "AndroSec1337 Cyber Team"
heder = {'X-Requested-With': 'XMLHttpRequest'}
waktumati = "60"

print("\n")
print("Submiting With [\033[32;1m"+haiker+"\033[0m] - [\033[32;1m"+tim+"\033[0m]\n\n")
print("-"*60)
time.sleep(3)

list = open(sys.argv[1], 'r')
while True:
	f = list.readline().replace('\n','')
	if not f:
		break
	faker = {'attacker': haiker, 'team': tim, 'poc': 'SQL Injection', 'url': f}
	try:
		asct = xi4u7.post(kontolz, timeout=80, data=faker, headers=heder)
	except Exception as gblk:
		print("\033[31;1m[ERROR]\033[0m "+str(gblk))
	else:
		result = re.findall(r"\">(.*)<span", asct.text, re.M|re.I)[0]
		if 'sukses' in asct.text.lower():
			print("\033[32;1m[SUKSES]\033[0m "+f)
		else:
			print("\033[3;1m[GAGAL]\033[0m "+f)
print("-"*60)
