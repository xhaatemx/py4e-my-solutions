import sys, os
from sys import argv


def main():
	# Use the file name mbox-short.txt as the file name
	Sums, counter = 0, 0
	fname = input("Enter file name: ")

	try:
		fh = open(fname)
	except:
		print('sorry file not found')
		return 1
	for line in fh:
		if not line.startswith("X-DSPAM-Confidence:") :
			continue
		number = float(line.strip('X-DSPAM-Confidence:'))
		Sums += number
		counter += 1

	print('Average spam confidence:', Sums/counter)
	return 0

if __name__ == '__main__':
	main()
