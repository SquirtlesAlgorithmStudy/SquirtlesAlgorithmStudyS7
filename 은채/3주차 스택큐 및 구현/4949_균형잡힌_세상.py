while True:
    sentence = input()
    stack = []
    flag = True

    if sentence == '.':
        break

    for s in sentence:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break

    print('yes' if not stack and flag else 'no')
