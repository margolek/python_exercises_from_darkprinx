"""

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

"""


def make_sequence(*args):

	return [x for x in args]

mylist = make_sequence(4,5,6,7,8,2,4)
print('My list: {}, My tuple: {}'.format(mylist,tuple(mylist)))