import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]


def bfs(r, c):
    answer = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q = deque()
    q.append((r, c))
    board[r][c] = "X"  # 어차피 이 문제에서는 BFS 한 번만 호출하니 Board에 방문 처리 가능
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == "X":
                    continue
                elif board[nr][nc] == "P":
                    answer += 1
                board[nr][nc] = "X"
                q.append((nr, nc))
    return answer if answer != 0 else "TT"


for i in range(N):
    for j in range(M):
        if board[i][j] == "I":
            print(bfs(i, j))
            break

# for issue
