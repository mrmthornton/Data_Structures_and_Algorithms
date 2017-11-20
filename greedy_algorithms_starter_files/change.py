# Uses python3
#import sys

def get_change(m):
    dimes = m//10
    m -= dimes * 10
    nickles = m//5
    m -= nickles * 5
    pennies = m
    return dimes + nickles + pennies

if __name__ == '__main__':
#    m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
