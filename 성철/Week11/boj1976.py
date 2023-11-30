# bfs 실행 후 여행 경로에 모든 지점이 방문처리 되어있지 않다면 no를 출력, 모든 지점이 방문처리 되어있다면 yes를 출력

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            graph[i].append(j)

visited = [False for _ in range(N)]
plan = list(map(int, input().split()))

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

bfs(plan[0]-1)
answer = True
for i in plan:
    if not visited[i-1]:
        answer=False
        break
if answer:
    print('YES')
else:
    print('NO')