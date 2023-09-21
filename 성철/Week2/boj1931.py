import sys
input = sys.stdin.readline

N = int(input())
li = []
for i in range(N):
    time = tuple(map(int, input().split()))
    li.append(time)

li.sort(key=lambda x: (x[1], x[0])) # 끝나는 순서대로 정렬

ans = 1
end = li[0][1] # 첫 회의

for i in range(1, N):
    # 현재 진행중인 회의가 끝나는 시간과 다음 회의의 시작시간 비교
    if li[i][0] >= end: 
        ans += 1
        end = li[i][1]
        # 회의 진행 카운트를 늘리고 끝나는 시간을 다음 회의의 끝나는 시간으로

print(ans)
