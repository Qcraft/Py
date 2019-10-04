#!/usr/bin/python3

citizen = input('are you a citizen? ')

if citizen.lower()  == 'yes':

	age = int(input('enter your age '))

	if age > 120:
	        print('dead or vampire')
	elif age > 17:
        	print('you can vote')
	elif age > 3:
        	print('to young')
	elif  age < 3:
		print('baby')
else:
	print('you can not vote')



