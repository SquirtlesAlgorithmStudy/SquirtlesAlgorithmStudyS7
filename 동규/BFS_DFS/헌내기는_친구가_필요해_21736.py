from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())
campus=[]
start=()
result=0

directions=[(0,1),(1,0),(0,-1),(-1,0)]

for row in range(N):
    cols=list(sys.stdin.readline().rstrip())
    for col in range(M):
        if cols[col]=="I":
            start=(row,col)
    campus.append(cols)
        

visited=[[False]*M for n in range(N)]
queue=deque([start])

def dfs(queue):
    while queue:
        x,y=queue.popleft()
        print(x,y)
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            
            if 0<= nx <M and 0<=ny<N:
                if campus[nx][ny]!="X" and not visited[nx][ny]:
                    queue.append((nx,ny))

            if campus[nx][ny]=="P":
                result+=1
    return result
print(dfs(queue))

