# 사각형 하나의 넓이는 100이고 겹치는 곳을 어떻게 찾을것인지가 중요
# 세개 이상의 종이가 겹쳐있을 수도 있음 -> 두개씩 비교해서 찾는 방법도 비효율적

# 한칸씩 체크를 한다?

import sys
input = sys.stdin.readline

N = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]
ans = 0

for _ in range(N):
    w, h = map(int, input().split())
    for i in range(w-1, w+9):
        for j in range(h-1, h+9):
            if arr[i][j] == 0:
                arr[i][j] = 1
                ans += 1

print(ans)