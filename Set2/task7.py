"""

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


"""

import numpy as np

class Array:

	mylist = []

	def __init__(self,row,column):
		self.row = row
		self.column = column

	def create_array(self):
	 
	 for i in range(self.row):
	 	for n in range(self.column):
	 		self.mylist.append(i*n)
	 return self.mylist

	def reshape(self):
		a = self.create_array()
		arr = np.array(a)
		arr1 = arr.reshape(self.row,self.column)
		return arr1
	def print_output(self):
		out = self.reshape()
		print(out)

myobject = Array(3,5)
myobject.print_output()



