import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)
def dfs(x,y):
    visited[x][y] = 1
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        Y,X = map(int, input().split())
        graph[X][Y] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
           if graph[i][j] == 1 and visited[i][j] == 0:
               dfs(i, j)
               ans += 1
    print(ans) 