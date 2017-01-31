

def merge(li1, li2):
	i,j=0,0
	listfinal=list()
	while i<len(li1) & j<len(li2):
		if li1[i]<li1[j]:
			listfinal.append(li1[i])
			i=i+1
		else:
			listfinal.append(li2[j])
			j=j+1
	listfinal=listfinal.append(li1[i:])
	return listfinal

def merge_sort(list1):
	if len(list1)==1:
		return list1
	i = len(list1)//2
	left_sub_list=merge_sort(list1[:i])
	right_sub_list1=merge_sort(list1[i:])
	merge(left_sub_list,right_sub_list1)

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
