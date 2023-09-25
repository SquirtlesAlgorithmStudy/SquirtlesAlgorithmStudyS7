import sys

N, L = map(int, sys.stdin.readline().split())
lo_list =[0]*N
result =0 # 0번째 인덱스에서 사용 

lo_list = list(map(int, sys.stdin.readline().split()))
lo_list.sort(reverse=False)

for i, curr in enumerate(lo_list):
    if i == 0:
        result +=1
        start = lo_list[0]
        continue
    diff = curr - start
    if diff >= L:
        start = curr
        result +=1

print(result)