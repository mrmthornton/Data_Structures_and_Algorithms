# python3

'''
algotithm:
    open = [ '[', '(', '{' ]
    close = [ ']', ')', '}' ]
    for char in string:
        if char in open:
            stack.push(char)
        else:
            if stack.empty(): return False
            top = stack.pop()
            if    top == '[' and char != ']' or \
                  top == '(' and char != ')'  or \
                  top == '{' and char != '}' : 
                return False
    return stack.empty()
'''
    
import sys

#### switch to list.append() and list.pop() , defaults are safer than explicit locations
def is_balanced(string:str) -> (int, bool) :
    opening = [ '[', '(', '{' ]
    closing = [ ']', ')', '}' ]
    stack = []
    for i,char in enumerate(string):
        if char in opening:
            stack.insert(0,(i,char))
        elif char in closing:
            if len(stack)==0: 
                return (i, False)
            top = stack.pop(0)
            if    top[1] == '[' and char != ']' or \
                  top[1] == '(' and char != ')'  or \
                  top[1] == '{' and char != '}' : 
                return (i, False)
    if len(stack)!=0:
        return (stack.pop(0)[0], False)
    return (-1, True)
        

if __name__ == "__main__":
    #text = sys.stdin.read()
    text = input()

    check = is_balanced(text)
    if check[1] is True:
        print("Success")
    else:
        print(check[0]+1)

