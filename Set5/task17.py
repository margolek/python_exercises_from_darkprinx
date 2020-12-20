"""

Write a program that computes the net amount of a bank account based
a transaction log from console input. The transaction log format is
shown as following:

D 100
W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500

"""
def read():
	"""Gets infromation from user"""
	balance = 0
	while True:
		x = input('Put "D" to deposit, "W" to withdrawal or "Q" to quit program:')
		if x == 'D':
			dep= input('Put value to deposit: ')
			balance +=int(dep)
		elif x == 'W':
			wit= input('Put value to withdrawal: ')
			balance -=int(wit)
		elif x == 'Q':
			break
		elif x != 'D' or x!= 'W' or x != 'Q':
			print('Incorrect value, choose correct')
			

	return balance

value1 = read()
print(value1)

