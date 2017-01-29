def twodpeak(start, end , list1):

    i= (start+end)//2
    maxim= max(list1[i])
    index=list1[i].index(max(list1[i]))
    if  (i - 1) >= 0 and (i + 1) < len(list1):
        if list1[i-1][index] > maxim:
            end = i - 1
            return twodpeak(start,end,list1)
        elif list1[i+1][index] > maxim:
            start = i + 1
            return twodpeak(start,end,list1)
    return list1[i][index]




def main():
    rows = input("Enter the no. of rows:- ")
    cols = input("Enter the no. of cols:- ")
    num_array = list()
    for i in range(int(rows)):
        print("Input in row ",int(i+1))
        sublist=list()
        for j in range(int(cols)):
            n = input("number :")
            sublist.append(int(n))
        num_array.append(list(sublist))
    print(num_array)
    peak=twodpeak(0,len(num_array)-1, num_array)
    print(peak)


if __name__=="__main__":
    main()
