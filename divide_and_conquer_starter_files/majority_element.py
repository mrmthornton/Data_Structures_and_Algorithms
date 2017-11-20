# Uses python3
import sys

#def get_majority_element(a, left, right):
#    if left == right:
#        return -1
#    if left + 1 == right:
#        return a[left]
#    #write your code here
#    return -1
def get_majority_element(a):
    number_count ={}
    n = len(a)
    half = int(n/2)
    
    for i in range(len(a)):
        if a[i] in number_count:
            number_count[a[i]] += 1
        else:
            number_count[a[i]] = 1
            
        if number_count[a[i]] > half:
                return 1
    return 0
        

def test_get_majority_elements():
    pass
    
    
if __name__ == '__main__':
    data_input = sys.stdin.read()
    #data_input = input("enter n followed by n ints: ")
    n, *a = list(map(int, data_input.split()))
    if n == 0:
        test_get_majority_elements()
    if n > 0:
        print(get_majority_element(a))

