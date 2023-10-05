# import sys
# import re

# fastin=sys.stdin.readline().rstrip()

fastin = """So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
."""
input_string = list(fastin)
length = len(input_string)

input_string.insert(0,' ')
input_string.pop()
a = 0
b = 0
bracket = ['(', ')','[',']',' ','.', '\n']

#print(input_string)
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
            else:
                print('no')
                a=0
                b=0
    