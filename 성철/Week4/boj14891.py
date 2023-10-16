# 백준 톱니바퀴


# deque를 활용 - rotate 함수를 사용하여 회전을 시킬 수 있음
# queue.rotate(-1): 반시계방향 회전 , queue.rotate(1): 시계방향 회전

# 맞닿아 있는 톱니바퀴
# wheel[0][2] wheel[1][6]
# wheel[1][2] wheel[2][6]
# wheel[2][2] wheel[3][6]

# N극이 0 S극이 1
# 1번이 회전하면 2번 -> 3번 -> 4번 순서대로 회전하는지 확인
# 2번이 회전하면 1번, 3번 -> 4번 순서대로 확인
# 3번이 회전하면 2번 4번, -> 1번 순서대로 확인
# 4번이 회전하면 3 2 1 순서대로 확인

from collections import deque
import sys

input = sys.stdin.readline

gear_list = []

for _ in range(4):
    li = list(input().rstrip())
    queue = deque(li)
    gear_list.append(queue)

N = int(input()) # 회전수

for _ in range(N):
    gear, direction = map(int, input().split())

    if gear == 1:
        if gear_list[0][2] != gear_list[1][6]:
            direction_1 = direction * -1
            if gear_list[1][2] != gear_list[2][6]:
                direction_2 = direction_1 * -1
                if gear_list[2][2] != gear_list[3][6]:
                    direction_3 = direction_2 * -1
                    gear_list[3].rotate(direction_3)

                gear_list[2].rotate(direction_2)

            gear_list[1].rotate(direction_1)

    elif gear == 2:
        if gear_list[0][2] != gear_list[1][6]:
            direction_1 = direction * -1
            gear_list[0].rotate(direction_1)
        if gear_list[1][2] != gear_list[2][6]:
            direction_2 = direction * -1
    
            if gear_list[2][2] != gear_list[3][6]:
                direction_3 = direction_2 * -1
                gear_list[3].rotate(direction_3)

            gear_list[2].rotate(direction_2)
    elif gear == 3:
        if gear_list[2][2] != gear_list[3][6]:
            new_direction = direction * -1
            gear_list[3].rotate(new_direction)
        if gear_list[1][2] != gear_list[2][6]:
            direction_2 = direction * -1
            
            if gear_list[0][2] != gear_list[1][6]:
                direction_3 = direction_2 * -1
                gear_list[0].rotate(direction_3)
            gear_list[1].rotate(direction_2)
    else: # gear == 4
        if gear_list[2][2] != gear_list[3][6]:
            direction_1 = direction * -1
            
            if gear_list[1][2] != gear_list[2][6]:
                direction_2 = direction_1 * -1
                
                if gear_list[0][2] != gear_list[1][6]:
                    direction_3 = direction_2 * -1
                    gear_list[0].rotate(direction_3)
                gear_list[1].rotate(direction_2)
            gear_list[2].rotate(direction_1)

    gear_list[gear-1].rotate(direction)
    

ans = 0
for i in range(4):
    if gear_list[i][0] == '1':
        ans += 2 ** i
    

print(ans)
#print(gear_list)
