import sys
N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
K = int(input())

result =0

for i in range(N):
    if num_list[i] == K:
        result +=1
        
print(result)