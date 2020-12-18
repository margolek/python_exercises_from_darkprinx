"""

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world

Practice makes perfect

Then, the output should be:

HELLO WORLD

PRACTICE MAKES PERFECT

"""

def get_value():
	""" This funtion gets input from user"""
	mylist = []
	while True:
		line = input('Put your sentence or put "q" to quit programm: ')
		if line == 'q':
			break
		else:
			mylist.append(line)
	return mylist

def read():
	a = get_value()
	
	for i in a:
		print(i.upper())

read()
