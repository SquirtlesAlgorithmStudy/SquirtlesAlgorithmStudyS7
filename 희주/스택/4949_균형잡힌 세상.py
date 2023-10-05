
while True:
    flag = 1
    stack = []
    S = input()
    
    for s in S:
        if s == '(' or s =='[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
            
    if S == '.':
        break
    
    print('yes' if not stack and flag else 'no')