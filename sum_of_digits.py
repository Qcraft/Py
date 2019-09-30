#!/usr/bin/python3

value = input()

value1 = 0

array = list(value)

for i in range(len(array)):
    value1 = value1 + int(array[i])

print(value1)
