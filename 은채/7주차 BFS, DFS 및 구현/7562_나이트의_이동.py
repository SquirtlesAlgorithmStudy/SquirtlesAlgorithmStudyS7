from collections import deque

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        if x == reachX and y == reachY:
            return graph[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


N = int(input())

for _ in range(N):
    I = int(input())
    x, y = map(int, input().split())
    reachX, reachY = map(int, input().split())

    graph = [[0] * I for _ in range(I)]
    graph[x][y] = 1

    print(bfs(x, y))

# 시간: 1284ms
