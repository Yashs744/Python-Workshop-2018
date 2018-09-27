# Functions
'''
	Resource:
		- https://www.programiz.com/python-programming/function
		- https://www.learnpython.org/en/Functions
'''

def greetings ():
	'''
		Greet the Person.
	'''
	print ("Hello user to the world of Python Programming")


greetings()

#-------------------------------------------------------------------#

def greetings (user_name):
	'''
		Greet the Person.
	'''
	print (f"Hello {user_name} to the world of Python Programming")


greetings("Yash Sharma")

#-------------------------------------------------------------------#

def add(x, y):
	return x+y

def subtract(x, y):
	return x-y;

def multiply(x, y):
	return x*y;

print (add(10, 3))
print (subtract(10, 3))
print (multiply(10, 3))

#-------------------------------------------------------------------#