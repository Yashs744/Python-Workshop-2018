# Lists 
''' 
	Resouce: 
		- https://realpython.com/python-lists-tuples/
		- https://www.programiz.com/python-programming/methods/list
'''

squares = [1, 4, 8, 16, 25, 36, 49]

print (squares)

for sq in squares:
	print (sq)


# Append Method
squares.append(64)
squares.append(81)

# Insert Method
# name_of_list.insert(index, element)
squares.insert(9, 100)
squares.insert(0, 0)

print (squares)

# Remove Method
# name_of_list.remove(element)
squares.remove(25)

print (squares)