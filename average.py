#!/usr/bin/python3

average = 0
number = 0
array = []

while number != "done":
	array.append(float(number))

	number = input()

for i in range (len(array)):

	average = average + array[i]

average = average / (len(array) - 1)

print(average)
