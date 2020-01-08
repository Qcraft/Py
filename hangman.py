#!/usr/bin/python3

import random

word = random.choices(['house', 'libary', 'apartment', 'yacht', 'horse', 'school', 'computer', 'linux'])
word = word[0]
guessword = '_' * len(word)
guessword = list(guessword)
attempt = 0

while word != ''.join(guessword):
	guess = input(''.join(guessword) + ' pick a letter: ')
	attempt = attempt + 1
	for i in range(len(word)):
		if guess == word[i]:
			guessword[i] = word[i]
print(attempt)
