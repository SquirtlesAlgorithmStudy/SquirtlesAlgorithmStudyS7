expression = input()
sum_list = []
temp = ""
# 숫자, 연산자 끼리 나누어 리스트에 저장
for i in range(len(expression)):
    if expression[i] == '+':
        temp = int(temp)
        sum_list.append(temp)
        sum_list.append('+')
        temp = ""
    elif expression[i] == '-':
        temp = int(temp)
        sum_list.append(temp)
        sum_list.append('-')
        temp = ""
    else:
        if i == len(expression)-1:
            temp = temp + expression[i]
            temp = int(temp)
            sum_list.append(temp)
            temp = ""
        temp = temp + expression[i]

# -가 나오는 뒷부분의 연산자를 제외한 숫자는 전부 음수로 변환
result = 0
flag = 0
for i in range(len(sum_list)):
    
    if sum_list[i] == '-':
        flag = 1
    elif flag == 1 and sum_list[i] != '+':
        sum_list[i] = -(sum_list[i])
    elif sum_list[i] == '+':
        continue
    
# 리스트의 요소중 연산자가 아닌 숫자만 더하는 과정
for item in sum_list:
    if isinstance(item, int):
        result += item
print(result)
#0925 변경사항 수정