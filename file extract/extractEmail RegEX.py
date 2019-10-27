import re
emails = []
host = []
fname = input('File name: ')
if len(fname) <= 0: fname = '1.txt'

file = open(fname)

# Extract emails
for line in file:
	if not re.search('^From ', line): continue
	line = line.lstrip('From ')
	emails += re.findall('\S+@\S+', line)

# Extract Hosts
for email in emails:
	host+= re.findall('@(\S+)', email)

