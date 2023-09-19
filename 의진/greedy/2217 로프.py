import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort()
answer = 0
scaler = N
for rope in ropes:
    answer = max(answer, scaler * rope)
    scaler -= 1

print(answer)

# Friday Clear
# Monday Clear
