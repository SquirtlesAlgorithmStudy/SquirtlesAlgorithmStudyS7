n = int(input())
houses = [list(map(int,input().split())) for _ in range(n)]
dp = [houses[0]]

for i in range(1, n):
    R = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
    G = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
    B = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]
    dp.append([R, G, B])

print(min(dp[-1]))