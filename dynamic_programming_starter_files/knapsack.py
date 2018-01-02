# Uses python3
import sys

def optimal_weight(W, w):
    n = len(w)
    w.insert(0,0)
    v = w.copy()
    value = [[0 for col in range(n+1)] for row in range(W+1)] 
    
    for i in range(1,n+1):
        for weight in range(1,W+1):
            value[weight][i] = value[weight][i-1]
            if w[i] <= weight:
                val = value[weight-w[i]][i-1] + v[i]
                if value[weight][i] < val:
                    value[weight][i] = val
    return value[W][n]
    
    return value

def less_than_optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    data_input = sys.stdin.read()
    #data_input = input("data in : ")
    W, n, *w = list(map(int, data_input.split()))
    #print(less_than_optimal_weight(W, w))
    print(optimal_weight(W, w))
