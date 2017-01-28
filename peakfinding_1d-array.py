


def peakfinder(start,end,arr):
	if end-start==1:
		if start==0:
			return start
		else:
			return end
	i=(start+end)//2

	if arr[i]<arr[i-1]:
		return peakfinder(start,i,arr)
	if arr[i]<arr[i+1]:
		return peakfinder(i,end,arr)
	else:
		return i



def main():
	num_array = list()
	num = input("Enter the no. of elements in the array:- ")
	print ('Feed the numbers in array:- ')
	for i in range(int(num)):
	    n = input("number :")
	    num_array.append(int(n))
	print ('Current status of the array is:- ',num_array)
	peak=peakfinder(0,len(num_array),num_array)
	print("Peak element of the array is:- ",num_array[peak])



if __name__=="__main__":
	main()
