from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())
campus=[]
start=()


directions=[(0,1),(1,0),(0,-1),(-1,0)]

for row in range(N):
    cols=list(sys.stdin.readline().rstrip())
    for col in range(M):
        if cols[col]=="I":
            start=(row,col)
    campus.append(cols)
        
visited=[[False]*M for n in range(N)]
queue=deque([start])
visited[start[0]][start[1]]=True

def dfs(queue):
    result=0
    while queue:
        x,y=queue.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<= nx <N and 0<=ny<M:
                if campus[nx][ny]=="P" and not visited[nx][ny]:
                    result+=1
                if campus[nx][ny]!="X" and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
    return result

res=dfs(queue)
if res>0:
    print(res)
else:
    print("TT")

