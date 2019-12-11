#!/usr/bin/python3

for i in range(1,10001):
	x = str(i ** 2)
	if len(x) % 2 != 0:
		x = '0' + x
	y = x[:(len(x)//2)]
	z = x[(len(x)//2):]
	if int(y) + int(z) == int(i):
		print(i)
