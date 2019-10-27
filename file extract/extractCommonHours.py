hours = []
common = {}
name = input("Enter file:")
if len(name) < 1 : name = "1.txt"
file = open(name)


# extract Senders Data
for line in file:
	if not line.startswith('From '): continue

	line = line.strip('From ').split()
	# add each hour into a list
	hours.append(line[4][: line[4].index(':')])

for h in hours:
	if h not in common.keys(): common[h] = 1
	else: common[h] += 1

common = dict(list(sorted(common.items())))
for (k, v) in common.items():
	print(k, v)

