import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
score = [[-1] * M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dice = [0, 1, 2, 3, 4, 5, 6]


def rolling(dice, direction, cur_r, cur_c):
    if direction == 0:  # 동
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    elif direction == 1:  # 남
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]
    elif direction == 2:  # 서
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif direction == 3:  # 북
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]

    return (cur_r + dr[direction], cur_c + dc[direction])


def bfs(r, c):
    queue = deque()
    tracking = []

    queue.append((r, c))
    tracking.append((r, c))
    score[r][c] = 0

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and score[nr][nc] == -1 and board[nr][nc] == board[r][c]:
                queue.append((nr, nc))
                tracking.append((nr, nc))
                score[nr][nc] = 0

    for tr, tc in tracking:
        score[tr][tc] = len(tracking)


if __name__ == "__main__":
    for i in range(N):
        for j in range(M):
            if score[i][j] == -1:
                bfs(i, j)

    direction = 0
    answer = 0
    cur_r = 0
    cur_c = 0
    for _ in range(K):
        if (cur_r + dr[direction] < 0) or (cur_r + dr[direction] >= N) or (cur_c + dc[direction] < 0) or (cur_c + dc[direction] >= M):
            direction = (direction + 2) % 4

        cur_r, cur_c = rolling(dice, direction, cur_r, cur_c)
        answer += (board[cur_r][cur_c] * score[cur_r][cur_c])

        if dice[6] > board[cur_r][cur_c]:
            direction = (direction + 1) % 4
        elif dice[6] < board[cur_r][cur_c]:
            direction = (direction - 1) % 4

    print(answer)
