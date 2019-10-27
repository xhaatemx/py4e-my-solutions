count = 0
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "1.txt"

fh = open(fname)
for line in fh:
	if not line.startswith('From '): continue
	line = line.split('From ')
	email = line[1][: line[1].index(' ')]
	print(email)
	count += 1
print("There were", count, "emails are extracted")
