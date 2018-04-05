'''The file contains the implementation of open addressing using 
array data structure to reduce the complexity of array search which
is O(n) in general case'''

import numpy as np

# hash function for open addressing
def hashing(item, size, val):
	i = (item%11 + val*(item%10 + val))%size
	return i

# inserting a value to the array
def insert(value, arr):
	key = hashing(value, len(arr[0]), 0)
	if arr[1][key]>0:
		print "Already occupied cell ", key
		for i in range(1, len(arr[0])):
			print "Already occupied cell ", key
			key = hashing(value, len(arr[0]), i)
			if arr[1][key] == 0:
				print "value ", value," inserted at ", key
				arr[0][key] = value
				arr[1][key] = 1
				break
	else:
		print "value ", value, "inserted at ", key
		arr[0][key] = value
		arr[1][key] = 1

	
# searching a value through the array
def search(value, arr):
	for i in range(len(arr[0])):
		key = hashing(value, len(arr[0]), i)
		if arr[1][key] == 0:
			print "Value ",value ,"does not exist"
			break
		elif (arr[1][key] == 1) and (arr[0][key] == value):
			print "Value ", value, " found at ", key
			break
		else:
			print "Searching for next value"

# delete a particular value from the array
def delete(value, arr):
	for i in range(len(arr[0])):
		key = hashing(value, len(arr[0]), i)
		if (arr[1][key] == 1) and (arr[0][key] == value):
			arr[0][key] = 0
			arr[1][key] = 0
			print "Value ", value, " deleted from ", key
			break
		
			

if __name__ == "__main__":
	arr = np.zeros((2, 10))
	insert(100, arr)
	insert(200, arr)
	insert(211, arr)
	insert(100, arr)
	insert(500, arr)
	insert(670, arr)
	insert(400, arr)
	search(211, arr)
	search(1004, arr)
	delete(211, arr)
	delete(400, arr)
	print arr
    	
