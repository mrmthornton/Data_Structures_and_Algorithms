# Uses python3
import sys
import random
import time

def partition3(a, L, r):
    x = a[L]
    j = L; k = L
    for i in range(L+1,r+1):
        if a[i] <= x:
            j += 1;k += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            a[i], a[k] = a[k], a[i]
            k += 1
        else:
            #k += 1
            pass
    a[L], a[j] = a[j], a[L]
    return (j,k)
            

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1,m2 = partition3(a, l, r)
    randomized_quick_sort3(a, l, m1 - 1);
    randomized_quick_sort3(a, m2 + 1, r);

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition2 
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

def test_randomized_quick_sort3():
    random.seed(1)
    a = [random.randint(0,10) for _ in range(1000)]
    b = a.copy()
    start=time.time()
    randomized_quick_sort3(a, 0, len(a)-1)
    finish=time.time()
    print("{:.10}".format(finish-start))
    start=time.time()
    randomized_quick_sort3(b, 0, len(a)-1)
    finish=time.time()
    print("{:.10}".format(finish-start))


if __name__ == '__main__':
    data_input = sys.stdin.read()
    #data_input = input("n and n ints : ")
    n, *a = list(map(int, data_input.split()))
    if n == 0:
        test_randomized_quick_sort3()
    else:
        randomized_quick_sort(a, 0, len(a)-1)
        #randomized_quick_sort3(a, 0, len(a)-1)
        for x in a:
            print(x, end=' ')
