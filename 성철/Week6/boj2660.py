import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[0] * N for _ in range(N)]


while 1:
    A,B = map(int, input().split())
    if A == -1 and B == -1:
        break
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

# 같은 행 또는 열에서 연결되어있는 친구들을 찾아야함
# 모든 인원에 대해 BFS로 순회하면서 가장 깊을때의 깊이가 몇인지 구해야함

def bfs(start):
    visited = [False] * N
    queue = deque()
    queue.append(start)
    visited[start] = True
    depth = [0] * N

    while queue:
        current = queue.popleft()

        for i in range(N):
            if graph[current][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
                depth[i] = depth[current] + 1

    return max(depth)

score_list = []

for i in range(N):
    score = bfs(i)
    score_list.append(score)

ans = min(score_list)

cnt = score_list.count(ans)

print(ans, cnt)

li = []

for i, score in enumerate(score_list):
    if score == ans:
        print(i+1, end=' ')

