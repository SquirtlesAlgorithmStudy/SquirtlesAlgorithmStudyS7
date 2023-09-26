equation = str(input())

eq_split = equation.split('-')

ans = 0

for i in eq_split[0].split('+'):
    ans += int(i)
    
for i in eq_split[1:]:
    new_list = i.split('+')
    for j in new_list:
        ans -= int(j)
        
print(ans)



