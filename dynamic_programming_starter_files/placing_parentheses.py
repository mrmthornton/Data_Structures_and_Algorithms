# Uses python3
import copy


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(i,j,M,m,ops):
    Min = float('inf')
    Max = float('-inf')

    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], ops[k-1])
        b = evalt(M[i][k], m[k+1][j], ops[k-1])
        c = evalt(m[i][k], M[k+1][j], ops[k-1])
        d = evalt(m[i][k], m[k+1][j], ops[k-1])
        Min = min(Min,a,b,c,d)
        Max = max(Max,a,b,c,d)

    return(Min,Max)
    
    
def get_maximum_value(dataset):
    
    d = list(map(int,dataset[0::2]))
    ops = dataset[1::2]
    n = len(d)
    M = [[0 for col in range(n+1)] for row in range(n+1)]

    for i in range(1,n+1):
        M[i][i] = d[i-1] # list 'd' uses 0 indexing
    
    m = copy.deepcopy(M)
    
    for s in range(1,n):
        for i in range(1,n+1-s):
            j = i + s
            Min,Max = MinAndMax(i,j,M,m,ops)
            m[i][j], M[i][j] = Min,Max
    
    return M[1][n]


if __name__ == "__main__":
    print(get_maximum_value(input()))

