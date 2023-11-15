import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) # 보드의 가로, 세로 길이
K = int(sys.stdin.readline().rstrip()) # 사과의 갯수

MAP = [[0]*N for _ in range(N)] # 사과 지도 
snake = [0]*N**2 # 뱀 지도 

for _ in range(K):
    x, y = sys.stdin.readline().rstrip().split(' ')
    MAP[int(x)-1][int(y)-1] = 2 # 사과 위치

L = int(sys.stdin.readline().rstrip()) # 방향 변환 횟수 

lotation = deque([]) 

for _ in range(L):
    sec, direc = sys.stdin.readline().rstrip().split(' ')
    lotation.append([int(sec), direc]) 

now_sec = 0 
now_r, now_c = 0, 1 # 시작 위치 
direction = 'R' # 처음 진행 방향
snake_tail = 0
snake.append([0,0]) # 뱀 출발 위치 

while True:
    now_sec += 1
    
    if now_r >= 0 and now_c >= 0 and now_r < N and now_c < N:
        if [now_r,now_c] in snake: # 뱀 자신과 충돌하면 종료
            print(now_sec) 
            break
        elif MAP[now_r][now_c] == 2: # 사과
            MAP[now_r][now_c] = 0 # 사과 없어짐
            snake.append([now_r, now_c]) # 머리 추가 
            snake_tail += 1 # 꼬리 위치 기억

        else: # 아무것도 없음
            snake.pop(-snake_tail-1) # 전진하면서 꼬리 이동
            snake.append([now_r,now_c]) # 왼쪽에 추가
        
        if len(lotation) > 0: # 방향 전환이 남았다면    
            if now_sec != lotation[0][0]: 
                if direction == 'R':
                    now_c += 1
                elif direction == 'L':
                    now_c -= 1
                elif direction == 'U':
                    now_r -= 1
                elif direction == 'D':
                    now_r += 1
            elif now_sec == lotation[0][0]: # 방향 전환 시 
                _, now_lot = lotation.popleft()
                if direction == 'R':  # 현재 방향 
                    if now_lot == 'L': # 방향 전환
                        now_r -= 1
                        direction = 'U'
                    else:
                        now_r += 1
                        direction = 'D'
                elif direction == 'L':
                    if now_lot == 'L':
                        now_r += 1
                        direction = 'D'
                    else:
                        now_r -= 1
                        direction = 'U'
                elif direction == 'U':
                    if now_lot == 'L':
                        now_c -= 1
                        direction = 'L'
                    else:
                        now_c += 1
                        direction = 'R'
                elif direction == 'D':
                    if now_lot == 'L':
                        now_c += 1
                        direction = 'R'
                    else:
                        now_c -= 1
                        direction = 'L'
        
        else: # 방향 전환이 더 이상 필요없다면 방향 유지해서 이동
            if direction == 'R':
                now_c += 1
            elif direction == 'L':
                now_c -= 1
            elif direction == 'U':
                now_r -= 1
            elif direction == 'D':
                now_r += 1
    else: # 범위 벗어나면 종료
        print(now_sec)
        break