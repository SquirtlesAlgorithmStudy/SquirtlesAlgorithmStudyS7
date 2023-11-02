import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, end1, end2):
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0
    queue = deque()
    queue.append((x, y))

    dx = [1, 2, -1, -2, 1, 2, -1, -2]
    dy = [2, 1, 2, 1, -2, -1, -2, -1]

    while queue:
        current = queue.popleft()

        if current[0] == end1 and current[1] == end2:
            print(visited[current[0]][current[1]])
            return

        for i in range(8):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[current[0]][current[1]] + 1

                
T = int(input())

for _ in range(T):
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    bfs(x1, y1, x2, y2)


    