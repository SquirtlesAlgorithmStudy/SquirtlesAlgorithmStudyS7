import sys

N = int(input())
meeting = []
result = 1 # N 은 1 이상

for _ in range(N):
    start, finish = list(map(int,sys.stdin.readline().split()))
    meeting.append([start, finish])

# meeting.sort(key=lambda x: [x[0], x[1]]) # 시간 초과 
meeting.sort(key=lambda x: [x[1], x[0]]) # 더 빨리 끝나는 순으로 정렬

pre_s, pre_f = meeting[0] # 무조건 
for j in range(1,N):
    post_s, post_f = meeting[j]
    if pre_f <= post_s:
        pre_s = post_s
        pre_f = post_f
        result +=1

print(result)