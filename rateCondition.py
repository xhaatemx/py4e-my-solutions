h = float(input('Enter work hours: '))
r = float(input('Enter Rate: '))


if h > 40.0:
	pay = (h * r) + ((h - 40.0) * (r * 0.5))
else:
	pay = h * r

print('Payment', pay)
