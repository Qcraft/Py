#!/usr/bin/python3

import random

count = 0
number = random.randrange(0,101)

while True:
	userinput = int(input('enter a number '))
	if userinput == number:
		print('correct ' + str(count))
		break
	elif userinput > number:
		print('lower')
	else:
		print('greater')
	count = count + 1
