"""

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5
between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

"""

def number():
	"""my solution"""
	mynumber = []
	for i in range(2000,3200):
		if i%7 == 0 and i%5 != 0:
			mynumber.append(i)
	print(mynumber,sep=',')


def number1():
	"""different option using generators and list comprehension"""

	#[f(x) if condition else g(x) for x in sequence]

	#[f(x) for x in sequence if condition]
	mylist = [x for x in range(2000,3200) if x%7 == 0 and x%5 != 0]
	print(mylist,sep = ',')



number()
print()
number1()

