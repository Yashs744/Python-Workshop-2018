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

## Arbitary Objects
items = ['apples', 'cake', 10, 3 + 4j, ['Ice Cream'], ['Cold Coffee', 'Ice Tea']]

print (items)

## Indexing
# Elements are Ordered and can be accessed via index starting from 0 to n-1
print (item[0]) # this would return the 1st elements in the items list
print (item[0:3]) # return first, second and third element from the list

# List also support negative indexing
print (item[-1]) # -1 represents last element in the list

# One can traverse in list using negative indexes
print (item[-3: -1])

# we can combine both
print (items[0:-3])

# stride
# Print List in Reverse Order
print (items[::-1])