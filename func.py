#!/usr/bin/python3

def foo(*UV):
	for i in range (len(UV)):
		print(UV[i])

foo(1, 3, 2, 7)
