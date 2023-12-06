n = int(input())
glasses = [0]
for _ in range(n):
    glasses.append(int(input()))
dp = [0]

if n == 1:
    print(glasses[n])
elif n == 2:
    print(glasses[n] + glasses[n-1])
else:
    for i in range(1, 3):
        dp.append(dp[i-1] + glasses[i])
    for i in range(3, n+1):
        dp.append(max(dp[i-1], dp[i-2] + glasses[i], dp[i-3] + glasses[i-1] + glasses[i]))
    
    print(max(dp))