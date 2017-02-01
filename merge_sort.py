#----------------------Merge Sort------------------------
'''The following code implemenets merge sort which is a 
sorting algorithm having worst case performance of O(nlog(n))
by implementing the divide and conquer strategy'''

# The function restitches the list to a sorted manner
def merge(left, right):
	sorted_list=[]
	left_ind,right_ind=0,0
	while left_ind<len(left) and right_ind<len(right):
		
		if left[left_ind] < right[right_ind]:
			sorted_list.append(left[left_ind])
			left_ind+=1
		else:
			sorted_list.append(right[right_ind])
			right_ind+=1
	if left:
		sorted_list.append(left[left_ind:])
	if right:
		sorted_list.append(right[right_ind:])
	return sorted_list

# The function makes a recursive call to itself to break the main unsorted list to smaller lists
def merge_sort(list1):
	if len(list1)<=1:
		return list1
	i = len(list1)//2
	left=list1[:i]
	right=list1[i:]
	left=merge_sort(left)
	right=merge_sort(right)

	return list(merge(left,right))

def main():
	num_array = list()
	num = input("Enter the no. of elements in the array:- ")	# the length of the number list
	print ('Feed the numbers in array:- ')	# input of the numbers
	for i in range(int(num)):
	    n = input("number :")
	    num_array.append(int(n))	#input number is appended to the list
	print ('Current status of the array is:- ',num_array)
	sorted_list=merge_sort(num_array)	# function call to merge_sort and storing the ret. value in sorted_list
	print("Sorted list is:- ",sorted_list)	# printing the sorted list

if __name__=="__main__":
	main()
