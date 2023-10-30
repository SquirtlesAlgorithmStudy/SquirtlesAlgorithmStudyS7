import sys
from collections import deque

N,K= map(int,sys.stdin.readline().split())
queue=deque([N])
directions=[-1,1,2]
time=1
count=0
while queue:
    X=queue.popleft()
    
    for direction in directions:
        if direction==1 or direction==-1:
            queue.append(X+direction)
        elif direction==2:
            queue.append(X*2)
        count+=1
    print(count)
    print(queue)
    if K in queue:
        print(time)
        break
    if count==time*3:
        time+=1
        count=0