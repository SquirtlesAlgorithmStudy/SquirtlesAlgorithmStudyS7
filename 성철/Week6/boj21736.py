# NxM크기 상하좌우 이동, 벽으로는 이동 못함

# O: 빈공간, X: 벽, I: 주인공, P: 다른 사람
# I가 움직여서 P를 만나야함
# I가 만날수 있는 사람 수 출력
# 아무도 만나지 못한 경우 TT 출력

import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    global ans
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] != 'X' and visited[nx][ny] == 0:
                if graph[nx][ny] == 'P':
                    ans += 1
                dfs(nx, ny)


N, M = map(int, input().split())

graph = []
ans = 0
for _ in range(N):
    s = list(input().rstrip())
    graph.append(s)

visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            dfs(i,j)

if ans == 0:
    print('TT')
else: print(ans)