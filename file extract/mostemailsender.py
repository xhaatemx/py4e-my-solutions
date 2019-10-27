emails = []
Email = {}
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "1.txt"

fh = open(fname)

for line in fh:
	if not line.startswith('From '): continue
	line = line.split('From ')
	emails.append(line[1][: line[1].index(' ')]) 


for email in emails:
	if email not in Email.keys():
		Email[email] = 1
	else: 
		Email[email] += 1

print(Email)		

for key in Email.keys():
	if Email[key] == max(Email.values()):
		MaxKey = key
		MaxValue = Email[key]

print(MaxKey, MaxValue)
