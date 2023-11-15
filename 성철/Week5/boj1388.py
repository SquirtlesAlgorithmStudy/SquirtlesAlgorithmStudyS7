import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0

def dfs(x,y):
    global cnt
    if visited[x][y] == True:
        return
    visited[x][y] = True
    if graph[x][y] == '-':
        # '-' 인 경우 가로로 탐색을 진행
        if y+1 < m and graph[x][y+1] == '-':
            dfs(x, y+1)
        else:
            cnt += 1
    else: # graph[x][y] == '|'
        # '|' 인 경우 세로로 탐색을 진행
        if x+1< n and graph[x+1][y] == '|':
            dfs(x+1,y)
        else:
            cnt+=1



for i in range(n):
    for j in range(m):
        dfs(i,j)

print(cnt)
