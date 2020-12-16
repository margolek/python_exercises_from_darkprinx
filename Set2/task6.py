"""

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 C D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:
100,150,180

The output of the program should be:

18,22,24

"""
import math as m

class EquationSolver:
	#Add feature to match functionality based on *args in
	#standard function
	#Values should be not put as a list
	def __init__(self,*args):
		self.args = args

	def print_value(self):
		print(list(self.args))

myobject = EquationSolver(4,5,3,2,6)
myobject.print_value()