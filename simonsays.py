#!/usr/bin/python3

while True:

	text = input("Simon Says: ")

	if text.lower() == "quit":
		print("Game Over")
		break
	print(text)
