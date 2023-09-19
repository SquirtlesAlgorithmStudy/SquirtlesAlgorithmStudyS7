import re
string = input()

numbers = re.findall('\d+',string)
alphabets = re.findall(r'([-,+])',string)
n = len(alphabets)
numbs = [int(numbers[i]) for i in range(n+1)] # int 형 numbers


# 여기까지 입력
check = []
if n>1:
    for i in range(n-1):
        if(alphabets[i]=='-' and alphabets[i+1]=='+'):
            check.append(int(i)) # - , + 조합 시작점 체크!

result = numbs[0]

for i in check: # - 뒤에 연이어있는 +들 다 -로 바꿔주기
    a = i
    while 1==1:   
        if(alphabets[a+1] != '-'):
            alphabets[a+1] = '-'
        else:
            break
        if(a>=n-2):
            break
        else:
            a+=1

for i in range(n): # 최종 값계산하기
    if(alphabets[i] == '+'):
        result+= numbs[i+1]
    else:
        result-= numbs[i+1]
print(result)