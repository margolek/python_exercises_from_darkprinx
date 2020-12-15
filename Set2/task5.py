"""

Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""
class MyClass:

	def __init__(self,input):
		self.input = input

	def getString(self):

		return str(self.input)

	def print_output(self):

		a =  self.getString()
		print('My string value with upper case: {}'.format(a.upper()))

myobject = MyClass('I am really curious if this code will be fine')
myobject.print_output()