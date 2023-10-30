sequence = int(input())
number_list = list(map(int,input().split()))
operator_list = list(map(int,input().split()))
operator = []
for i in range(operator_list[0]):
    operator.append('+')
for i in range(operator_list[1]):
    operator.append('-')
for i in range(operator_list[2]):
    operator.append('*')
for i in range(operator_list[3]):
    operator.append('/')
    
from itertools import permutations

# 가능한 조합 생성
possible_combinations = set(permutations(operator))

def cal(num1,num2,operator):
    if operator == '+':
        return int(num1+num2)
    elif operator == '-':
        return int(num1-num2)
    elif operator == '*':
        return int(num1*num2)
    elif operator == '/':
        if num1 <0:
            return -int(-(num1)/num2)
        else:
            return int(num1/num2)
        
result = []
for j in possible_combinations:
    number = 0
    for i in range(len(number_list)-1):
        if i == 0:
            number = cal(number_list[i],number_list[i+1],j[i])
        else:
            number = cal(number,number_list[i+1],j[i])

    result.append(number)

print(max(result))
print(min(result))

