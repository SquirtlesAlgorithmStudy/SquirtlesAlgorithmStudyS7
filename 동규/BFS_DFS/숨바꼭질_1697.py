import sys
from collections import deque

N,K= map(int,sys.stdin.readline().split())
queue=deque([N])
dist=[0]*100001

def dfs():
    while queue:
        X=queue.popleft()
        if X==K:
            print(dist[X])
            break
        for dX in (X+1,X-1,X*2):
            if 0<=dX<=100000 and not dist[dX]:
                
                dist[dX]=dist[X]+1
                queue.append(dX)
dfs()
