import re


sums = 0
fname = input('File name: ')
if len(fname) <= 0: fname = '2.txt'

file = open(fname)

# Extract nums and add them to a summtion
for line in file:
	for n in re.findall('[0-9]+', line):
		sums += int(n)


print(sums)
