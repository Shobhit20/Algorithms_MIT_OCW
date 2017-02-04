#--------------------Heap Sort--------------------
'''The heap sort algorithm is a sorting algorithm having a worst 
case time complexity of O(nlog(n)). The algorithm is implemented 
using a data structure called heaps whicha are binary trees with 
some fixed property '''

# The function checks for the left and right sub child in order to build a max heap. A max heap satisfies the property that the child are always smaller than the parent
def maxheapify(list1,length,i):
    left_child=2*i+1    # The left child of parent i
    right_child=2*i+2   # The right child of parent i
    if left_child<=(length-1) and list1[i]<list1[left_child]:
        largest=left_child
    elif right_child<=(length-1) and list1[i]<list1[right_child]:
        largest=right_child
    else:
        largest=i
    if largest!=i:
        list1[i],list1[largest]=list1[largest],list1[i]     #swapping the child with value greater than parent with the parent
        maxheapify(list1,length,largest)

# The function sorts the unsorted array
def heap_sort(list1,length):
    for i in range(len(list1)):
        list1[0],list1[length-1]=list1[length-1],list1[0]   #swapping of the first element(largest) and last element(smallest) of the array
        length=length-1     # Decreasing the size of list
        maxheapify(list1,length,0)
    return list1

# The function calls the maxheapify to build a max heap and then calls the heap_sort to sort the list
def build_maxheap(list1):
    length=len(list1)   
    for i in range((len(list1)-1)//2,-1,-1):
        maxheapify(list1,length,i)
    return list(heap_sort(list1,length))


def main():
    num_array = list()
    num = input("Enter the no. of elements in the array:- ")    # the length of the number list
    print ('Feed the numbers in array:- ')  # input of the numbers
    for i in range(int(num)):
        n = input("number :")
        num_array.append(int(n))    #input number is appended to the list
    print ('Current status of the array is:- ',num_array)
    sorted_list=build_maxheap(num_array)   # function call to build_maxheap and storing the ret. value in sorted_list
    print("Sorted list is:- ",sorted_list)  # printing the sorted list

if __name__=="__main__":
    main()
