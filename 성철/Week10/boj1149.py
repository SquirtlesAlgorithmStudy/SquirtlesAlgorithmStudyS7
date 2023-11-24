## BOJ 1149: RGB 거리
## Silver 1

# 집 N개, 1번집부터 N번집 순서
# 집은 빨초파 3개 중 하나의 색
# 빨초파 각각의 비용이 주어짐

# 규칙
# 이웃한 집의 색깔은 다름

import sys

input = sys.stdin.readline

N = int(input())

price = [[0]]
dp = [[0] * 3 for _ in range(1002)]


for _ in range(N):
    p = list(map(int, input().split()))
    price.append(p)

# 집이 두개일 때
# 01,02,12,10,20,21 6가지 경우 중 가장 작은것

# 집이 세개일때
# 010, 012, 020, 021, 120,121, 101,102, 201, 202, 210, 212

dp[2][0] = price[2][0] + min(price[1][1], price[1][2])
dp[2][1] = price[2][1] + min(price[1][0], price[1][2])
dp[2][2] = price[2][2] + min(price[1][0], price[1][1])

flag = [[1,2], [0,2], [0,1]]

if N > 2:
    for i in range(3, N+1):
        for j in range(3):
            dp[i][j] = price[i][j] + min(dp[i-1][flag[j][0]], dp[i-1][flag[j][1]])

print(min(dp[N]))
