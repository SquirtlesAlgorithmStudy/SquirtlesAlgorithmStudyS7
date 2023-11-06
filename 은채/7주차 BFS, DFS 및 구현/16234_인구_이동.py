from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    union = []
    queue.append((x, y))
    union.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == 0:
                if abs(graph[nx][ny] - graph[x][y]) >= L and abs(graph[nx][ny] - graph[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))

    return union


answer = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union_countrys = bfs(i, j)

                if len(union_countrys) > 1:
                    flag = True
                    population = sum(
                        graph[x][y] for x, y in union_countrys) // len(union_countrys)

                    for x, y in union_countrys:
                        graph[x][y] = population

    if not flag:
        print(answer)
        break

    answer += 1

# 시간: 5652ms
