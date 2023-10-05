import sys
input=sys.stdin.readline().rstrip()
num = 0

str = list(input)
length = len(str)
pointer = 0
for i in range(2):
    str.append('-')

def count_and_pop(a):
    global num, pointer
    num += 1
    pointer += a
    for i in range(a):
        str.pop(0)

while pointer < length:
    if str[0] == 'c':
        if str[1] == '=' or str[1] == '-':
            count_and_pop(2)
        else:
            count_and_pop(1)
    elif str[0] == 'd':
        if str[1] == '-':
            count_and_pop(2)
        elif str[1] == 'z' and str[2] == '=':
            count_and_pop(3)
        else:
            count_and_pop(1)
        
    elif str[0] == 'l' and str[1] == 'j':
        count_and_pop(2)
    elif str[0] == 'n' and str[1] == 'j':
        count_and_pop(2)
    elif str[0] == 's' and str[1] == '=':
        count_and_pop(2)
    elif str[0] == 's' and str[1] == '=':
        count_and_pop(2)
    elif str[0] == 'z' and str[1] == '=':
        count_and_pop(2)
    else:
        count_and_pop(1)

print(num)
    
            
            
        