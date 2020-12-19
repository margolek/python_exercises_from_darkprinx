"""

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!

Then, the output should be:

UPPER CASE 1

LOWER CASE 9

"""

def read():
	"""Read sentence from user"""
	a = input('Put your sentence: ')
	return [n for n in a]


def count():
	"""Count upper and lower letters"""
	a = read()
	upper,lower = 0,0
	for i in a:
		if i.isupper():
			upper+=1
		elif i.islower():
			lower+=1
	return upper,lower;


def print_out():
	"""Print out feedback to user"""
	up,low = count()
	print("In your sentence is: \nupper case: {} \nlower case: {}".format(up,low))

print_out()