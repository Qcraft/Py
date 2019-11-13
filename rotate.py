#!/usr/bin/python3

word = input()

output = ''

for i in range((len(word)//2), len(word)):
	output = output + word[i]
for i in range((len(word)//2)):
	output = output + word[i]
print(output)
