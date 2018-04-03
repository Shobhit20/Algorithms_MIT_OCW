
import random
def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1          # count occurences
    i = 0
    print(count)
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array

def main():
    num_array = random.sample(range(1, 100),30)   #input number is appended to the list
    num_array = counting_sort(num_array,max(num_array))
    print(num_array)

if __name__ == "__main__":
    main()
