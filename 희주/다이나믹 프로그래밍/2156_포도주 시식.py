# dp 문제 
# 답안 참고함
import sys 

N =int(input())
wine_list =[0] +[int(input()) for _ in range(N)]

dp =[0] *(N+1)

for i in range(1, N+1):
    if i ==1:
        dp[i] =wine_list[1]
        continue
    elif i ==2:
        dp[i] =wine_list[1] +wine_list[2]
        continue
    
    dp[i] =max(dp[i-1], dp[i-2]+wine_list[i], dp[i-3] +wine_list[i-1] +wine_list[i])
        
print(dp[-1])