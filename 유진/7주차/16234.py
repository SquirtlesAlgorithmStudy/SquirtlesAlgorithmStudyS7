import sys
import math
from collections import deque



n, l, r = map(int, sys.stdin.readline().split())  

arr = list()
a_list = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    union = [(i, j)]
    count = arr[i][j] 
       
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기 
                union.append((nx, ny))
                visit[nx][ny] = True
                dq.append((nx, ny))
                count += arr[nx][ny]
    # 연합 국가 간 인구수 계산  
    for x, y in union:
        arr[x][y] = math.floor(count / len(union))

    return len(union)

result = 0    # 인구 이동이 발생하는 일수 
while True:   # 인구 이동이 없을 때까지 반복 
    visit = [[False] * n for _ in range(n)]
    flag = False  # 인구 이동 존재 유무 플래그 
    # 맨 처음 나라부터 하씩 방문하여 bfs진행
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:   # 인구 이동이 없는 경우 break
        break
    result += 1

print(result)