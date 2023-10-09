import re

fastin=[]
while 1==1:
    a = list(input())
    fastin += a + ["\n"]
    if(a == ["."]):
        break

input_string = list(fastin)
length = len(input_string)

input_string.insert(0,' ')
input_string.pop()
a = 0
b = 0
bracket = ['(', ')','[',']',' ','.', '\n']

length = len(input_string)

for i in range(1,length-1):
    if input_string[i-1] in bracket or input_string[i+1] in bracket:
        if(input_string[i]=='('):
            a+=1
        elif(input_string[i]==')'):
            if a>0:
                a-=1
            else:
                a = -100
                
        elif(input_string[i]=='['):
            b+=1
        elif(input_string[i]==']'):
            if b>0:
                b-=1
            else:
                b = -100
        elif(input_string[i]=='.'):
            if(a==0 and b==0):
                print('yes')
                a=0
                b=0
            else:
                print('no')
                a=0
                b=0
    