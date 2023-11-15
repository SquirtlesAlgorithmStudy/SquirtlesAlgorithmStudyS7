import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

from collections import deque

# dx,dy 설정
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(sx, sy, ex, ey):
    if sx == ex and sy == ey: # 시작 좌표가 도착 좌표와 일치하면 도착
        return 0
    queue = deque([(sx, sy)]) # 시작 x,y 좌표
    visited = [[False] * l for _ in range(l)] # 체스판 길이(l*l)에 따라 visited 초기화
    visited[sx][sy] = True # 시작 좌표 방문처리
    move = 0
    while queue: # queue가 빌때까지
        move += 1
        for _ in range(len(queue)): # bfs, 같은 level에서만 반복할 수 있게 설정. 같은 move내에서의 queue의 길이.
            x, y = queue.popleft()
            for i in range(8): # dx,dy 8가지 방향
                nx, ny = x + dx[i], y + dy[i]
                if nx == ex and ny == ey:
                    return move # 도착! 
                if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]: # l*l을 벗어나지 않고 방문처리 안했으면 방문
                    visited[nx][ny] = True # 방문 처리
                    queue.append((nx, ny)) # 큐에 넣기


T = int(input())
for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(sx, sy, ex, ey))
