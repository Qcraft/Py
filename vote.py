#!/usr/bin/python3

age = int(input('enter your age '))

if age < 3:
	print('baby')
elif age < 10:
	print('child')
elif age > 100:
	print('dead')

citizen = input('are you a citizen? ')

if citizen == 'yes':
	if age > 18:
		print('you can vote')
	else:
		print('you can not vote')
else:
	print('ypu can not vote')
