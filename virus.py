#!/usr/bin/python3

day = 1
num = 7700000
infected = 1
temp = 0

while temp <= num:
	infected = 2 * infected
	temp = infected + temp
	day = day + 1
print(day)
