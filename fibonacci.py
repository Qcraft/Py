#!/usr/bin/python

num0 = 0
num1 = 1
num3 = 0

for i in range (11):
	num3 = num1 + num0
	num0 = num1
	num1 = num3
	print(num3) 
