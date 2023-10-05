num = int(input())
time = []

for i in range(num):
    start, end = map(int, input().split())
    time.append([start, end])

# 종료 시간 오름차순 정렬 후, 시작 시간이 빠른 회의 오름차순 정렬
time=sorted(time, key=lambda x: (x[1],x[0])) 

count = 1
end_time = time[0][1]

for i in range(1,num):
    if time[i][0] >= end_time:
        count+=1
        end_time = time[i][1]

print(count)