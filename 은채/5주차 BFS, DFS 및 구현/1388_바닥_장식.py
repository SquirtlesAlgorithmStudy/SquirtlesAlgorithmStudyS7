N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]


def dfs(x, y):

    if floor[x][y] == '-':
        floor[x][y] = 0

        if y+1 < M and floor[x][y+1] == '-':
            dfs(x, y+1)
        if y-1 > -1 and floor[x][y-1] == '-':
            dfs(x, y-1)

        return True

    elif floor[x][y] == '|':
        floor[x][y] = 0

        if x+1 < N and floor[x+1][y] == '|':
            dfs(x+1, y)
        if x-1 > -1 and floor[x-1][y] == '|':
            dfs(x-1, y)

        return True

    return False


answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            answer += 1

print(answer)
