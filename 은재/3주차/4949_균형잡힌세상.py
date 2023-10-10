while True:
    s = input()
    
    if s == '.': #입력의 종료 조건
        break
    
    stack = []
    
    for i in s: #문자열 내 요소 하나씩 검토
        
        #요소 i가 '(', '['일 경우 append
        if i == '(' or i == '[': 
            stack.append(i)
        
        elif i == ')':
            #요소 i가 ')'면서 stack이 존재하고 마지막 요소가 '('일 경우 마지막 요소 pop
            if stack and stack[-1] == '(':
                stack.pop()
            
            #이를 제외한 모든 경우 append
            else:
                stack.append(i)
                break
            
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                
            else:
                stack.append(i)
                break
            
    if stack: #stack이 존재할 경우 no 출력
        print("no")
    else: #stack이 존재하지 않는 경우 균형을 이루므로 yes 출력
        print("yes")