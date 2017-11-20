#Uses python3

import sys
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
            #print(L)
            #print(chunk_size)
            #print(data)
        break # comment out for continuous run0
    return(data)        


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
        
        
if __name__ == '__main__':
    #data_input = sys.stdin.read()
    data_input = input()
    data = data_input.split()
    if data[0]==str(0):
        data = test()
    else:
        data = ['0','1']
        #data = ['0','1','3']
        data = ['0','1','3','4']
    permutations = [check_all_permutations(data)]
    #perms = generate_all_permutations(data)
    print(data)
    print(permutations)
        