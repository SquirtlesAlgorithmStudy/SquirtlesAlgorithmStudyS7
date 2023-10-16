import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    global visited
    global cabbages
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이미 커버된 배추 
        if (nx, ny) in visited:
            continue
        # 연결된 배추 찾음
        if (nx, ny) in cabbages:
            visited.add((nx, ny))
            dfs(nx, ny)

T = int(input())
total_cabbages = []
for _ in range(T):
    M, N, K = map(int, input().split())
    total_cabbages.append(set([tuple(map(int, input().split())) for _ in range(K)]))

for cabbages in total_cabbages:
    visited = set()
    ret = 0
    for cabbage in cabbages:
        # 기저사례: 이미 모든 배추를 커버한 경우
        if len(visited) == len(cabbages):
            break
        if cabbage in visited:
            continue
        dfs(*cabbage)
        ret += 1
    print(ret)