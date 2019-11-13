#!/usr/bin/python3

string = input()
x = ''

for i in range (len(string), 0, -1):
	x = x + string[i-1]
if x == string:
	print('yes')
else:
	print('no')
