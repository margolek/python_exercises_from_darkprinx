"""

Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
>Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9

Then, the output should be:

1,9,25,49,81

"""

def input_user():
	"""Gets input from user"""
	a = input('Put values separated by comma: ')
	a = a.split(",")
	return [int(x)**2 for x in a if int(x)%2!=0]

def print_out():
	"""Print out feedback to user"""
	a = input_user()
	mylist = ','.join(map(str,a))
	print(mylist)

print_out()