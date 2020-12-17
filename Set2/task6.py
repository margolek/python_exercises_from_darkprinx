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

	c = 50 #Class variable
	h = 30

	def __init__(self,*args):
		self.args = args

	def calculate(self):

		return  [m.sqrt((2*self.c*d)/self.h) for d in self.args]

	def print_value(self):

		a = self.calculate()
		for i in a:
			if a.index(i) < len(a)-1:
				print(round(i),end =', ')
			else:
				print(round(i),end ='')

myobject = EquationSolver(100,150,180)
myobject.print_value()