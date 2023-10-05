import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    
    if sentence == '.':
        break

    stack = []

    for char in sentence:
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
        elif char == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

    if len(stack) == 0: print('yes')
    else: print('no')
    