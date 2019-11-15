#!/usr/bin/python3

min = 1
max = 100


while True:

	guess = (min + max) // 2
	x = input(guess)
	if x == '>':
		min = guess
	elif x == '<':
		max = guess
	else:
		break
