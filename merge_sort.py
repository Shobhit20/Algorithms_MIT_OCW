def merge(left, right):
	sorted_list=[]
	left_ind,right_ind=0,0
	while left_ind<len(left1) and right_ind<len(right):
		
		if left1[left_ind] < right[right_ind]:
			sorted_list.append(left1[left_ind])
			left_ind+=1
		else:
			sorted_list.append(right[right_ind])
			right_ind+=1
	if left1:
		sorted_list.extend(left1[left_ind:])
	if right:
		sorted_list.extend(right[right_ind:])
	return sorted_list

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
	sorted_list=merge_sort(num_array)	# function call to sortlist and storing the ret. value in peak
	print("Sorted list is:- ",sorted_list)	# printing the sorted list

if __name__=="__main__":
	main()
