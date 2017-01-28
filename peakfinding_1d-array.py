#----------------Peak Finder------------------

'''The following peak finding algorithm finds a single peak in O(log(n))
time rather than O(n). However any algorithm which finds all the peaks will 
take atleast O(n) time'''

# The following function finds the index of the peak by recursive calling and returns the index
def peakfinder(start,end,arr):
	if end-start==1:	# Check for the first and last index of sublist to be peak
		if start==0:	# start index is returned in case of start=0
			return start
		else:
			return end
	i=(start+end)//2	# //2 operator takes the floor divison with respect to 2

	if arr[i]<arr[i-1]:	#check for the left element for sublist return
		return peakfinder(start,i,arr)
	if arr[i]<arr[i+1]:	#check for the right element for sublist return
		return peakfinder(i,end,arr)
	else:
		return i

#input of number to the list and function call to the peakfinder() function 
def main():
	num_array = list()
	num = input("Enter the no. of elements in the array:- ")	# the length of the number list
	print ('Feed the numbers in array:- ')	# input of the numbers
	for i in range(int(num)):
	    n = input("number :")
	    num_array.append(int(n))	#input number is appended to the list
	print ('Current status of the array is:- ',num_array)
	peak=peakfinder(0,len(num_array)-1,num_array)	# function call to peakfinder and storing the ret. value in peak
	print("Peak element of the array is:- ",num_array[peak])	# printing the peak

if __name__=="__main__":
	main()

