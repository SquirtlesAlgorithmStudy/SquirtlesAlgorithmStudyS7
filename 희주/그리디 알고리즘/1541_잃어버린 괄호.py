cal = input().split('-') # - 를 기점으로 split
result = 0
result = sum(list(map(int,cal[0].split('+')))) # 첫번째 숫자는 반드시 더함

if len(cal) > 1: # + 연산 뿐이 없다면 pass 
    for n in cal[1:]:
        tmp = sum(list(map(int,n.split('+'))))
        result -=tmp

print(result)
