import sys
from collections import deque

members = int(input())
graph={member+1:[] for member in range(members)}
distances=[]

while True:
    f1,f2= map(int,sys.stdin.readline().split())
    if f1==-1 and f2==-1:
        break
    graph[f1].append(f2)
    graph[f2].append(f1)
print(graph)
def bfs(start):
    count=0
    length=0
    visited=[False for member in range(members)]
    queue=deque([start])
    
    while queue:
        print(queue)
        friends=queue.popleft()
        print(graph[friends])

        #length=len(graph[friends])

        if not visited[friends-1]:
            
            visited[friends-1]=True
            print(visited)
            count+=1
            queue.extend(graph[friends])
        if all(i==True for i in visited):
            break
    return count

for member in range(members):
    distance =bfs(member+1)
    distances.append(distance)
    print(distances)
