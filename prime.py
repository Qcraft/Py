#!/usr/bin/python3

for x in range(2,101):
	for f in range(2,int(x**0.5)+1):
		if x % f == 0:
			break
	else:
		print(x)
