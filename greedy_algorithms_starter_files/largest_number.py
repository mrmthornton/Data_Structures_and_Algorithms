#Uses python3

import sys
from functools import partial
import random


def test():
    random.seed(36963)
    while True:
        bignum = random.randint(0,sys.maxsize)
        bignum_str = str(bignum)
        print(bignum_str)
        data = []
        L = len(bignum_str)
        start=0
        while L>0:
            chunk_size = random.randint(1,L) 
            data.append(bignum_str[start:start+chunk_size])
            start = start+chunk_size
            L = L-chunk_size
        print("data = ",data)
        largest = largest_number(data)
        correct = nieve_largest_number(data)
        if largest == correct:
            print("OK!")
            continue
        else:
            print("ERROR:")
            print("nieve: ",correct)
            print("argor: ",largest)
            break
            

def total_order(longest, str_num):
    L = len(str_num)
    multiplier = longest//L + 1
    str_num_fill = "".join([str_num]*multiplier)
    str_num_fill = str_num_fill[:longest]
    #print(str_num_fill)
    return(float("0." + str_num_fill))
    
    
def largest_number(a):
    longest = len(sorted(a,key=len,reverse=True)[0])
    total_order_longest = partial(total_order,longest)
    b = sorted(a,key=total_order_longest ,reverse=True)
    res = "".join(b)
    return res


def check_all_permutations(collected):
    if len(collected)>1:
        results = []
        L = len(collected)
        for i in range(L):
            n=collected[i]
            local_collected = [collected[j] for j in range(L) if j != i]
            local_result = [n+s for s in check_all_permutations(local_collected)]
            [results.append(s) for s in local_result]
        return(results)
    else:
        return(collected)
    
    
def nieve_largest_number(data):
    data.sort(reverse=True)
    combinations = check_all_permutations(data)
    #print("combinations = ",combinations)
    combinations.sort(reverse=True)
    return combinations[0]
    

if __name__ == '__main__':
    #data_input = sys.stdin.read()
    data_input = input()
    data = data_input.split()
    if data[0]==str(0):
        test()
    else:
        a = data[1:]
        print(largest_number(a))
    