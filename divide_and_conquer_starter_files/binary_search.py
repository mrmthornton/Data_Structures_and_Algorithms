# Uses python3
import sys
import random


def binary_search(arr, key):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = int(left + (right - left)/2)
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def test_binary_search():
    for i in range(10):
        a = [n for n in range(1,10**5)]
        #print(a)
        xlist = [random.randint(1,10**6) for n in range(1000)]
        #print(xlist)
        ls = [linear_search(a, x) for x in xlist]
        bs = [binary_search(a, x) for x in xlist]
        #print(ls)
        print(bs)
        assert(ls == bs)
    
    
if __name__ == '__main__':
    '''
    
    '''
    data_in = sys.stdin.read()
    #data_in = input("Enter  n,A[n],m,X[m] or 0 for random testing: ")
    data = list(map(int, data_in.split()))
    
    n = data[0]
    if n == 0:
        test_binary_search()

    if n > 0:
        m = data[n + 1]
        a = data[1 : n + 1]
        #for x in data[n + 2:]:
        #    print(linear_search(a, x), end = ' ')
        for x in data[n + 2:]:
            print(binary_search(a, x), end = ' ')
