import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

gears = [input().strip() for _ in range(4)]
K = int(input())

for _ in range(K):
    num, direction = map(int, input().split())
    num -= 1  # 인덱스는 0부터 시작..

    # 반시계 방향 -1, 시계방항 +1
    directions = [0] * 4
    directions[num] = direction

    # 왼쪽 톱니바퀴 확인
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            directions[i-1] = -directions[i]
        else:
            break  # 같으면 중단(시간효율..)

    # 오른쪽 톱니바퀴 확인
    for i in range(num, 3):
        if gears[i][2] != gears[i+1][6]:
            directions[i+1] = -directions[i]
        else:
            break  # 같으면 중단(역시나 시간효율)

    # 회전
    for i in range(4):
        if directions[i] == 1:
            gears[i] = gears[i][-1] + gears[i][:-1]  # 시계 방향
        elif directions[i] == -1:
            gears[i] = gears[i][1:] + gears[i][0]  # 반시계 방향


score = sum([(2 ** i) * int(gear[0]) for i, gear in enumerate(gears)])
print(score)  