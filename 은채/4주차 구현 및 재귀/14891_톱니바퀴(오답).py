from collections import deque
import copy

wheels = [deque(list(map(int, input()))) for i in range(4)]
k = int(input())

for _ in range(k):
    origin = copy.deepcopy(wheels)
    idx, direction = map(int, input().split())
    idx = idx - 1

    wheels[idx].rotate(direction)

    if idx != 0:
        for i in range(idx-1, 0, -1):
            if origin[i][2] != origin[i+1][6]:
                if (idx-i) % 2 == 0:
                    wheels[i].rotate(direction)
                else:
                    wheels[i].rotate(-1 * direction)
            else:
                break

    if idx != 3:
        for i in range(idx+1, 3):
            if origin[i-1][2] != origin[i][6]:
                if (idx-i) % 2 == 0:
                    wheels[i].rotate(direction)
                else:
                    wheels[i].rotate(-1 * direction)
            else:
                break

answer = 0
for i in range(4):
    answer += wheels[i][0] * (2**i)

print(answer)
