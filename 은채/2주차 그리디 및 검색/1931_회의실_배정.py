N = int(input())
times = []
answer = 1

for i in range(N):
    s, e = map(int, input().split())
    times.append([s, e])

times.sort(key=lambda x: (x[1], x[0]))

finish = times[0][1]
for i in range(1, len(times)):
    if times[i][0] >= finish:
        answer += 1
        finish = times[i][1]

print(answer)