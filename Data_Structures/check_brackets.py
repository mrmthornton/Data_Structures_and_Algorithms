# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

    
def is_balanced(string):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        #print(i)
        if next == '(' or next == '[' or next == '{':
            # push onto stack
            opening_brackets_stack.insert(0, Bracket(next,i))
            #print("pushing")
            
        #if len(opening_brackets_stack)==0:
        #    print('0')
            
        if next == ')' or next == ']' or next == '}':
            # check against top of stack
            if len(opening_brackets_stack)==0:
                return 0
            
            if opening_brackets_stack[0].Match(next) == True:
                opening_brackets_stack.pop(0)
                #print("popping")
            else: 
                return opening_brackets_stack[0].position+1
    if len(opening_brackets_stack)>0:
        return len(opening_brackets_stack)
    else: return True
        

if __name__ == "__main__":
    #text = sys.stdin.read()
    text = input()

    check = is_balanced(text)
    if check is True:
        print("Success")
    else:
        print(check)
