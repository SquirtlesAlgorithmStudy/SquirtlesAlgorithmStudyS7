from collections import deque

def bfs(x, y):
    Queue = deque()
    Queue.append((x,y))

    while Queue:
        x, y = Queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                Queue.append((nx, ny))

T = int(input())

for _ in range(T):

    M, N, K= map(int, input().split())

    graph = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)