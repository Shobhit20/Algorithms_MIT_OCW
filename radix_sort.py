def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = int(arr[i]/exp1)
        count[ (index)%10 ] += 1

    for i in range(1,10):
        count[i] += count[i-1]
 
    i = n-1
    while i>=0:
        index = int(arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
    return output
 

def radix_sort(num_arr):
    exp=1
    maxim=max(num_arr)
    while maxim/exp > 0:
      num_arr= countingSort(num_arr,exp)
      exp *= 10
    return num_arr


def main():
    num_array = list()
    num = input("Enter the no. of elements in the array:- ")    # the length of the number list
    print ('Feed the numbers in array:- ')  # input of the numbers
    for i in range(int(num)):
        n = input("number :")
        num_array.append(int(n))    #input number is appended to the list
    num_array = radix_sort(num_array)
    print(num_array)

if __name__ == "__main__":
    main()
