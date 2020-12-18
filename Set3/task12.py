"""

Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.The numbers obtained should be printed
in a comma-separated sequence on a single line.

"""
"""
#simple example how to use lambda and filter together
li = [1,2,3,4,5]
mylist = list(filter(lambda x:x%2 == 0,li))
print(mylist)
"""

def num2str():
	return [str(x) for x in range(1000,3001)]		

def check_even():
	a = num2str()
	return list(filter(lambda x: all(int(j)%2==0 for j in x),a))

def print_even():
	numbers = check_even()
	print(numbers)

print_even()


