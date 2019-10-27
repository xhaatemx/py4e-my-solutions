lst = list()

def main():
	fname = input("Enter file name: ")
	if len(fname) < 1: fname = "3.txt"
	try:
		fh = open(fname)
		for line in fh:
			line = line.split('\n')
			if line not in lst:
				line = line[0].split()
				for e in line:
					if e not in lst:
						lst.append(e)
		lst.sort()
		print(lst)
	except:
		print('No such file or directory')
		return 1
	return 0

if __name__ == '__main__':
	main()