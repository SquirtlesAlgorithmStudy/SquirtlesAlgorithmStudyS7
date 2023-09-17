N, L = map(int, input().split())
position = list(map(int, input().split()))

position.sort()

# first fix
cnt = 1
fix = position[0]

for i in position[1:]:
    if (fix+L-1) < i:
        cnt += 1
        fix = i

print(cnt)