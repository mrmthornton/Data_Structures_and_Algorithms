# Uses python3
import sys
import random

def merge(b,c):
    bn = len(b)
    cn = len(c)
    d = [0] * (bn+cn)
    bi = 0; ci = 0
    while bi < bn and ci < cn:
        if b[bi] <= c[ci]:
            d[bi+ci] = b[bi]
            bi += 1
        else:
            d[bi+ci] = c[ci]
            ci += 1
    if bi == bn:
        while ci < cn:
            d[bi+ci] = c[ci]
            ci += 1
    if ci == cn:
        while bi < bn:
            d[bi+ci] = b[bi]
            bi += 1 
    return d

def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    m = int(n/2)
    b = merge_sort(a[0:m])
    c = merge_sort(a[m:n])
    a_sorted = merge(b,c)
    return a_sorted


def merge_mod(b,c):
    bn = len(b)
    cn = len(c)
    d = [0] * (bn+cn)
    bi = 0; ci = 0
    count = 0
    '''
    for i in range(len(b)):
        for j in range(len(c)):
            if b[i] > c[i]:
                count += 1
    '''
    while bi < bn and ci < cn:
        if b[bi] <= c[ci]:
            d[bi+ci] = b[bi]
            bi += 1
        else:
            d[bi+ci] = c[ci]
            ci += 1
            count += (len(b)-bi)
    if bi == bn:
        while ci < cn:
            d[bi+ci] = c[ci]
            ci += 1
    if ci == cn:
        while bi < bn:
            d[bi+ci] = b[bi]
            bi += 1 
    return (d,count)

def merge_sort_mod(a):
    n = len(a)
    if n < 2:
        return (a,0)
    m = int(n/2)
    b,b_ = merge_sort_mod(a[0:m])
    c,c_ = merge_sort_mod(a[m:n])
    a_sorted,merge_count = merge_mod(b,c)
    local_sum = b_ + c_ + merge_count
    #print("merge_sort_mod: ",b_, c_, merge_count,'\t', local_sum, b, c)
    return (a_sorted, local_sum)
            
        
    

#def get_number_of_inversions(a, b, left, right):
#    number_of_inversions = 0
#    if right - left <= 1:
#        return number_of_inversions
#    ave = (left + right) // 2
#    number_of_inversions += get_number_of_inversions(a, b, left, ave)
#    number_of_inversions += get_number_of_inversions(a, b, ave, right)
#    #write your code here
#    return number_of_inversions
def get_number_of_inversions(a):
    x,invs = merge_sort_mod(a)
    return invs


def get_number_of_inversions_bruteforce(a):
    number_of_inversions = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                number_of_inversions += 1
    return number_of_inversions


def test_get_number_of_inversions():
    for _ in range(500):
        a = [random.randint(0,6) for _ in range(random.randint(1,1000))]
        b = a.copy()
        brute = get_number_of_inversions_bruteforce(a)
        smart = get_number_of_inversions(b)
        assert(brute==smart)

if __name__ == '__main__':
    
    #print(merge([1,2,3],[4,5,6]))
    #print(merge([1,3,5],[2,4,6]))
    #print(merge([1,4,5],[2,3,6]))
    #print(merge_sort([6,5,4,3,2,1]))
    #print(merge_mod([1,2,3],[4,5,6]))
    #print(merge_mod([1,3,5],[2,4,6]))
    #print(merge_mod([1,4,5],[2,3,6]))
    #print(merge_sort_mod([6,5,4,3,2,1]))
    
    data_input = sys.stdin.read()
    #data_input = input("n, n ints : ")
    n, *a = list(map(int, data_input.split()))

    if n == 0:
        test_get_number_of_inversions()
        
    else:
        #print(get_number_of_inversions_bruteforce(a))
        print(get_number_of_inversions(a))
    