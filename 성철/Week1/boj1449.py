N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cur_loc = arr[0]
cur_tape = L
ans = 1 # 첫 테이프

for i in range(1,N):
    cur_tape -= (arr[i] - cur_loc)
    # 남은 길이가 1보다 작은 경우 - 새로운 테이프
    cur_loc = arr[i]

    if cur_tape < 1:
        cur_tape = L
        ans += 1 # 새로운 테이프 시작

print(ans)

