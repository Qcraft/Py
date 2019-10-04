#!/usr/bin/python3

month = input().lower()

winter = ['dec', 'jan', 'feb']
spring = ['mar', 'apr', 'may']
summer = ['jun', 'jul', 'aug']
fall = ['sep', 'oct', 'nov']

if month in winter:
	print('winter')
elif month in spring:
	print('spring')
elif month in summer:
	print('summer')
elif month in fall:
	print('fall')
