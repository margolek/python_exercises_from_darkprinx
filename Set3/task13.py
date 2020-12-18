"""

Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10

DIGITS 3

"""

def read():
	"""Read values from user input"""
	a = input('Tape your input: ')
	return [str(x) for x in a]

def count():
	"""All necessary calculations"""
	a = read()
	let,dig = 0,0
	for i in a:
		if i.isalpha():
			let+=1
		elif i.isdigit():
			dig+=1
	return dig,let;

def result():
	"""Print out program result"""
	dig,let = count()
	print('In your sentence is: \n{} Digits \n{} Letter'.format(dig,let))


result()


