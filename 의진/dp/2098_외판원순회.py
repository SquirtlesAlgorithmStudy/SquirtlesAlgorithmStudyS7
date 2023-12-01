import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
dp = [[-1] * (1 << N) for _ in range(N)]


def dfs(city, visited):
    # Base Case
    if visited == (1 << N) - 1:
        if W[city][0]:
            return W[city][0]
        else:
            return INF

    if dp[city][visited] != -1:
        return dp[city][visited]

    # Recursive Case
    for next_city in range(1, N):
        if not W[city][next_city]:
            continue
        if visited & (1 << next_city):
            continue

        dp[city][visited] = INF if dp[city][visited] == -1 else dp[city][visited]

        dp[city][visited] = min(dp[city][visited], dfs(
            next_city, visited | (1 << next_city)) + W[city][next_city])

    if dp[city][visited] == -1:
        dp[city][visited] = INF
    return dp[city][visited]


print(dfs(0, 1))
