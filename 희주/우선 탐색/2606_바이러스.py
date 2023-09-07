import sys

node = int(input())
line = int(input())

result =set()
line_list =[[] for _ in range(node+1)]
check =[False]*(node+1)
stack =[]

for i in range (line):
    n, m = (map(int, sys.stdin.readline().split()))
    line_list[n].append(m)
    line_list[m].append(n)

check[1] =True
stack.append(1)

while stack:
    curr = stack.pop()
    
    for next in line_list[curr]:
        if check[next] ==False:
            check[next] =True
            stack.append(next)
            
print(check.count(True)-1)
