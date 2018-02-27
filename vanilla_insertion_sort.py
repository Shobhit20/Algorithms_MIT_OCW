#-----------------Insertion sort-------------------
'''The following algorithm sorts the unsorted array and is one of 
the most basic sorting algorithm. The algorithm is of O(n^2) 
complexity. Two operations take place:-
i) Traversing the list
ii) Comparison and swapping of the elements'''

import random

#The function takes unsorted array as input and sorts the array and returns the sorted array
def sortlist(list1):
	for i in range(1,(len(list1)-1)):
		j=i
		while j>0 and list1[j]<list1[j-1]:
			list1[j],list1[j-1] = list1[j-1],list1[j]	#swapping of the elements on the j and j-1 index
			j=j-1
	return list1

# function takes list as input and makes a function call to the sortlist function
def main():
	num_array = random.sample(range(1, 100),30)
	print ('Current status of the array is:- ',num_array)
	sorted_list=sortlist(num_array)	# function call to sortlist and storing the ret. value in peak
	print("Sorted list is:- ",sorted_list)	# printing the sorted list

if __name__=="__main__":
	main()
