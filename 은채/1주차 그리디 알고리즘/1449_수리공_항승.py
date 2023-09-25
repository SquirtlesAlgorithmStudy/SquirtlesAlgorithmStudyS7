N, L = map(int, input().split())
leaks = list(map(int, input().split()))
start = 0
cnt = 0

leaks.sort()
for l in leaks:
    if start < l:
        cnt += 1
        start = l + L - 1

print(cnt)
