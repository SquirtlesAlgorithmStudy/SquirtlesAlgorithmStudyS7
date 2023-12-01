import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c):
    if r == 0 and c == 0:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    result = 0
    for i in range(4):
        pr = r - dr[i]
        pc = c - dc[i]

        if 0 <= pr < M and 0 <= pc < N and board[pr][pc] > board[r][c]:
            if dp[pr][pc] != -1:
                result += dp[pr][pc]
            else:
                result += dfs(pr, pc)
    dp[r][c] = result
    return result


print(dfs(M-1, N-1)) 


