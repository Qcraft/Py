#!/usr/bin/python3

temp = 0
sum = 0
done = ' '

while True:
	temp = input()
	if temp == 'quit':
		print(sum)
		break
	sum = sum + int(temp)


