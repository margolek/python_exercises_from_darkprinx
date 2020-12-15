"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320

"""

def factorial(num):
	"""Best choice to factorial is use recursion"""
	if num == 0:
		return 1
	else:
		return num * factorial(num-1)

a = factorial(5)
print("result: {}".format(a))