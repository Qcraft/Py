#!/usr/bin/python3

word = input()
count = 0

for i in range (len(word)):
	if word[i] in 'aeiou':
		count = count + 1

print(count)
