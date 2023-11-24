## BOJ 1520 : 내리막 길
## Gold 3

# 그래프의 각 칸에 높이가 적혀있음
# 상하좌우 이동 가능

# 왼쪽 위 출발 오른쪽 아래 도착
# 항상 내리막길로 이동하는 경로가 몇개인지? 

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

M, N = map(int, input().split())
graph = []
for _ in range(M):
    l = list(map(int, input().split()))
    graph.append(l)

dp = [[-1] * N for _ in range(M)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    # 방문했던 칸은 또 방문하지 않는다
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[x][y] > graph[nx][ny]: 
                cnt += dfs(nx, ny)
    dp[x][y] = cnt
    return dp[x][y]

# 도착지점 표시
dp[M-1][N-1] = 1
print(dfs(0,0))

print(dp)


# dp[x][y] += dfs(인접하면서 높이가 낮은 지점)

