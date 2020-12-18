"""

Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world

"""

def get_string():
	a = input('Put your words separeted by space: ')
	mylist = a.split()
	return mylist


def delete_duplicate():
	a = get_string()
	myset = set(a)
	list_output = list(sorted(myset))
	return list_output

def display():
	a = delete_duplicate()
	for i in a:
		print(i,end=' ')


display()