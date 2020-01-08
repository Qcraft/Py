#!/usr/bin/python3

def findmin(*array):
	num = array[0]
	x = 0
	for i in range (len(array)-2):
		if num > array[i+1]:
			num = array[i+1]
		x = x + 1
	if num > array[-1]:
		num = array[-1]
	return num

print(findmin(5, 2, 3, 100, 1))
