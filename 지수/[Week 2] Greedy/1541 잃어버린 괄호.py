# 1541 잃어버린 괄호

s = input().split('-')                           

number = []
for i in s:
    number.append(sum(map(int,i.split('+'))))

result = number[0]
for i in number[1:]:
    result -= i

print(result)