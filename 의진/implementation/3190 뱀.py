import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apple_pos = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
commands = deque([tuple(input().split()) for _ in range(L)])

board = [[0] * N for _ in range(N)]
for row, col in apple_pos:
    board[row-1][col-1] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

direction = "0"
board[0][0] = 2
snake = {"head": [0, 0], "tail": [0, 0]}
time = 0
next_command = commands.popleft()
next_time = int(next_command[0])

while True:
    time += 1
    nr = snake["head"][0] + dr[int(direction[-1])]
    nc = snake["head"][1] + dc[int(direction[-1])]
    if nr == N or nc == N or nr == -1 or nc == -1:
        print(time)
        break
    if board[nr][nc] == 2:
        print(time)
        break

    if time == next_time:
        if next_command[1] == "L":
            direction += str((int(direction[-1]) - 1) % 4)
        elif next_command[1] == "D":
            direction += str((int(direction[-1]) + 1) % 4)
        if commands:
            next_command = commands.popleft()
            next_time = int(next_command[0])
    else:
        direction += direction[-1]

    if board[nr][nc] != 1:
        board[snake["tail"][0]][snake["tail"][1]] = 0
        tail_direction = int(direction[0])
        direction = direction[1:]
        snake["tail"][0] += dr[tail_direction]
        snake["tail"][1] += dc[tail_direction]

    snake["head"][0] = nr
    snake["head"][1] = nc

    board[nr][nc] = 2

# for issue
