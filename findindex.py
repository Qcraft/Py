#!/usr/bin/python3

l = [5, 3 ,1, 2, 6]

def findindex(l):
	small = l[0]
	for i in range(len(l)):
		if l[i] < small:
			small = l[i]
			index = i
	return index

print(findindex(l))
