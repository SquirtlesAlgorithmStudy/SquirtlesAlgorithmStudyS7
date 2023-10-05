expression = input().split('-')
numbers = []

for exp in expression:
    if exp.isdecimal():
        numbers.append(int(exp))
    else:
        l = list(map(int, exp.split('+')))
        numbers.append(sum(l))

result = numbers[0] - sum(numbers[1:])
print(result)
