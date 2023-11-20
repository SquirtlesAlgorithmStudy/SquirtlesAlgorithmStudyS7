import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n]%10007)

# 다른 사람 코드
# n = int(input())
# dp=[0,1,3]
# for i in range(3,n+1):
#     dp.append(dp[i-1] + dp[i-2]*2)
# print(dp[n]%10007)