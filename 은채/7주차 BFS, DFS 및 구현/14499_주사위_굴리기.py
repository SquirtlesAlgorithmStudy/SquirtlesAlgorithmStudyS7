N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

# 동 -> 4 2 1 6 5 3
# 서 -> 3 2 6 1 5 4
# 북 -> 5 1 3 4 6 2
# 남 -> 2 6 3 4 1 5

for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]

    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
    else:
        a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
        if command == 1:
            dice = [d, b, a, f, e, c]
        elif command == 2:
            dice = [c, b, f, a, e, d]
        elif command == 3:
            dice = [e, a, c, d, f, b]
        else:
            dice = [b, f, c, d, a, e]

        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[-1]
        else:
            dice[-1] = graph[nx][ny]
            graph[nx][ny] = 0

        x, y = nx, ny

        print(dice[0])

# 시간: 44ms
