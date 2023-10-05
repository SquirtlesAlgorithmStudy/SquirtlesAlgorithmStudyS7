i = 0
s = []

while(True):
    s.append(input())
    if(s[i] == "."):
        break
    i += 1

for j in range(i):
    answer = 1
    bracket = []
    for k in s[j]:
        if(k=='(' or k=='['):
            bracket.append(k)

        if(k==')'):
            if(len(bracket)>0 and bracket[-1]=='('):
                bracket.pop()
            else:
                answer = -1
        if(k==']'):
            if(len(bracket)>0 and bracket[-1]=='['):
                bracket.pop()
            else:
                answer = -1

    if(answer==1 and len(bracket)==0):
        print("yes")
    else:
        print("no")