
def maxheapify(list1,length,i):
    left_child=2*i+1
    right_child=2*i+2
    if left_child<=(length-1) and list1[i]<list1[left_child]:
        largest=left_child
    elif right_child<=(length-1) and list1[i]<list1[left_child]:
        largest=right_child
    else:
        largest=i
    if largest!=i:
        list1[i],list1[largest]=list1[largest],list1[i]
        maxheapify(list1,length,largest)

def heap_sort(list1,length):
    for i in range(len(list1)):
        list1[0],list1[length-1]=list1[length-1],list1[0]
        length=length-1
        maxheapify(list1,length,0)
    return list1

def build_maxheap(list1):
    length=len(list1)
    for i in range((len(list1)-1)//2,-1,-1):
        maxheapify(list1,length,i)
    return heap_sort(list1,length)


def main():
    num_array = list()
    num = input("Enter the no. of elements in the array:- ")    # the length of the number list
    print ('Feed the numbers in array:- ')  # input of the numbers
    for i in range(int(num)):
        n = input("number :")
        num_array.append(int(n))    #input number is appended to the list
    print ('Current status of the array is:- ',num_array)
    sorted_list=build_maxheap(num_array)   # function call to merge_sort and storing the ret. value in sorted_list
    print("Sorted list is:- ",sorted_list)  # printing the sorted list

if __name__=="__main__":
    main()
