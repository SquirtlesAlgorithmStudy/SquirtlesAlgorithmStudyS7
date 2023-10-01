import re

s = input()
expression = ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']
answer = 0

for exp in expression:
    c = re.findall(exp, s)
    answer += len(c)
    s = re.sub(exp, '_', s)

s = re.sub('_', '', s)
print(answer + len(s))
