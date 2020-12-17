"""

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated 
sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world

Then, the output should be:

bag,hello,without,world

"""
class Sorting():

	def __init__(self,*args):
		self.args = args

	def sort(self):
		mylist = sorted(list(self.args))
		return mylist

	def output(self):
		a = self.sort()
		print(a)

myobject = Sorting('bag','hello','output')
myobject.output()