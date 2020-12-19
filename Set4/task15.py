"""

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9

Then, the output should be:

7380

"""

def calculate_input():
	"""Gets input from user and calculate output value"""
	inp = input("Input your digit: ")
	return sum(int(inp)**x for x in range(1,5))


myvalue = calculate_input()
print(myvalue)

	
