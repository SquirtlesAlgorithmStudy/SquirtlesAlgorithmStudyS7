n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x:(x[1], x[0]))

max_mt=0
position = 0

for start in range(n):
    if(meeting[start][0] >= position):
        position = meeting[start][1]
        max_mt += 1

print(max_mt)