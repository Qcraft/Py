#!/usr/bin/python3

x = input().lower()

if x == 'dec' or x == 'jan' or x == 'feb':
	print('winter')
elif x == 'mar' or x == 'apr' or x == 'may':
	print('spring')
elif x == 'jun' or x == 'jul' or x == 'aug':
	print('summer')
elif x == 'sep' or x == 'oct' or x == 'nov':
	print('fall')
