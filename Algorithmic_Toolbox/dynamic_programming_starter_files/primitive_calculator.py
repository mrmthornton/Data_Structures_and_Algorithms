# Uses python3
import sys

def optimal_sequence(n):
    seq = [(0,0)] * (n+1)
    
    for i in range(1,n+1):
        
        count1 = (seq[i-1][0]+1, 1)
        seq[i] = count1
        
        if i%2==0:
            count2 = (seq[i//2][0]+1, 2)
            if count2[0] < seq[i][0]:
                seq[i] = count2
            
        if i%3==0:
            count3 =  (seq[i//3][0]+1, 3)
            if count3[0] < seq[i][0]:
                seq[i] = count3 
    
    numbers = []
    i = n
    while i >= 1:
        numbers.append(i)
        op = seq[i][1]
        if op == 1:
            i = i - 1
        if op == 2:
            i = i//2
        if op == 3:
            i = i//3
            
    return list(reversed(numbers))

    
    
def simple_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return list(reversed(sequence))

data_input = sys.stdin.read()
#data_input = input("data in : ")
data = list(map(int, data_input.split()))
n = data[0]

#simple = simple_sequence(n)
#print(len(simple) - 1)
#for x in simple:
#    print(x, end=' ')   
#print()

optimal = optimal_sequence(n)
print(len(optimal) - 1)
for x in optimal:
    print(x, end=' ')
