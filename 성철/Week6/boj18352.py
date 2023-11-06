import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
depth = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def bfs(start):
    visited[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()

        for adjacent in graph[current]:
            if visited[adjacent] == False:
                queue.append(adjacent)
                visited[adjacent] = True
                depth[adjacent] = depth[current] + 1

bfs(X)
ans = []
for index, distance in enumerate(depth):
    if distance == K:
        ans.append(index)
        print(index)

if len(ans) == 0:
    print(-1)
