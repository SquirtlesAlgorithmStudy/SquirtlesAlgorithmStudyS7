import sys

N = int(input())
k_list =[0]*N
K = N
result =0

for i in range(N):
    k_list[i] = int(input()) # 리스트로 저장 

k_list.sort(reverse=False) # 오름차순으로 정렬

i =0
while K >=1: 
    if K == 1:
        max_l = max(k_list)
        result = max(result, max_l)
        break
    else:
        result = max(result, k_list[i]*K) # k_list 에서 가장 K 번째로 작은 수와 비교 
        K -=1
        i +=1
    
print(result)