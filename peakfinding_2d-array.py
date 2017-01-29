#-----------------Peak finder 2-d array-----------------
''' The following algorithm finds a 2-d peak  in a 2d list
in a complexity of O(nlog(n)) instead of O(mn), where m and n 
are the rows and columns for the list'''

# The function returns the element which is a peak in the given 2-d list
def twodpeak(start, end , list1):

    i= (start+end)//2   # The // operator is used for floor division
    maxim= max(list1[i])    # Finds maximum element in the list
    index=list1[i].index(max(list1[i]))     #returns the index of maximum element in the list
    if  (i - 1) >= 0 and (i + 1) < len(list1):
        if list1[i-1][index] > maxim:   # a check to choose the left sublist or right sublist
            end = i - 1
            return twodpeak(start,end,list1)    #recursive call
        elif list1[i+1][index] > maxim:     # a check to choose the left sublist or right sublist
            start = i + 1
            return twodpeak(start,end,list1)    #recursive call
    return list1[i][index]      # Returns the peak element

# Calls the twodpeak function and stores the returned value in peak variable
def main():
    rows = input("Enter the no. of rows:- ")    # The no. of rows
    cols = input("Enter the no. of cols:- ")    # The no. of cols
    num_array = list()      # num_array is declared as a list object
    for i in range(int(rows)):
        print("Input in row ",int(i+1))
        sublist=list()
        for j in range(int(cols)):
            n = input("number :")
            sublist.append(int(n))
        num_array.append(list(sublist))
    print(num_array)
    peak=twodpeak(0,len(num_array)-1, num_array)    # function call to twodpeak function
    print(peak)


if __name__=="__main__":
    main()
