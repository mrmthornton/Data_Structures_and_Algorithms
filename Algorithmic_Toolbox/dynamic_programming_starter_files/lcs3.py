#Uses python3

import sys

def lcs3(a, b, c):
    print(a,b,c)
    
    return min(len(a), len(b), len(c))

if __name__ == '__main__':
    #data_input = sys.stdin.read()
    data_input = input()
    data = list(map(int, data_input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
