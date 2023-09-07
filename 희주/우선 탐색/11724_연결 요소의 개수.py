import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
graph_list =[0]+[[] for _ in range(N)]

for _ in range(L):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph_list[n1].append(n2)
    graph_list[n2].append(n1)

count =0
check =[False]*(N+1)

for i in range(1, N+1):
    if check[i] == True:
        continue
    
    deque_list = deque([i])
    check[i] =True
    while deque_list:
        n = deque_list.popleft()
        for next in graph_list[n]:
            if not check[next]:
                deque_list.append(next)
                check[next] =True
    count +=1
                
print(count)