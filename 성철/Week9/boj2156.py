# 연속해서 세잔을 마실 수 없다
# 각 포도주 잔에 들어있는 포도주의 양이 주어짐
# 최대한 많이 마실때 포도주의 양

import sys
input = sys.stdin.readline

n = int(input())

wine = [0] * 10002
for i in range(1,n+1):
    wine[i] = int(input())

# 한잔 -> 다마시면 됨
# 두잔 -> 다마시면 됨
# 세잔 -> 12 or 23 or 13
# 네잔 -> 124(dp[3]의 최대값이 12인 경우), 134(dp[3]의 최대값이 13인 경우), 23(dp[3]의 최대값이 23인 경우)


dp = [0] * 10002

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
else:
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    
    for i in range(3,n+1):

        dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])

    print(dp[n])
