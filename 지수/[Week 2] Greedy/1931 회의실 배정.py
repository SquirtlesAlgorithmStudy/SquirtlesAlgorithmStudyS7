# 1931 회의실 배정

n = int(input())
time = list(list(map(int, input().split())) for _ in range(n))

time.sort(key=lambda x: (x[1], x[0])) # 두번째 값을 기준으로 오름차순 정렬, 두번째 값이 같을 경우 첫번째 값을 기준으로 오름차순 정렬

current = time[0]
count = 1

for next in time[1:]:
    if current[1] <= next[0]:
        current = next
        count += 1

print(count)