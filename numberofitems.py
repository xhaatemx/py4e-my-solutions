List = [1, 2, [3, 4, 5], 6]
num = 0

for i in range(len(List)):
	try:
		int(List[i])
		num += 1
	except:
		for i in List[i]:
			num += 1

print(num)


