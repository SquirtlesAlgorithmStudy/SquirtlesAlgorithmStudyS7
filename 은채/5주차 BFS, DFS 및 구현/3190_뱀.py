from collections import deque

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
info = dict()
for _ in range(L):
    X, C = input().split()
    info[int(X)] = C

snake = deque()
snake.append([0, 0])
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = 0
sec = 0

while True:
    sec += 1
    start = snake.popleft()
    d = directions[direction % 4]
    reach = [start[0] + d[0], start[1] + d[1]]

    if (-1 in reach) or (N in reach) or (reach in snake):
        break

    snake.appendleft(start)
    snake.appendleft(reach)

    if board[reach[0]][reach[1]] == 0:
        snake.pop()
    else:
        board[reach[0]][reach[1]] = 0

    if sec in info.keys():
        if info[sec] == 'D':
            direction += 1
        else:
            direction += 3

print(sec)
