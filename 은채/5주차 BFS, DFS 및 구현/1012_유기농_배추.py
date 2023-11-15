import sys

sys.setrecursionlimit(100000)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    def dfs(x, y):
        if x <= -1 or y <= -1 or x >= M or y >= N:
            return False

        if field[x][y] == 1:
            field[x][y] = 2

            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x, y-1)

            return True

        return False

    answer = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                answer += 1

    print(answer)
