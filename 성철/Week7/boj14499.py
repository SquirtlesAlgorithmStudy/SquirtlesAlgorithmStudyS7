# 입력 세로N, 가로M, 주사위 x,y 좌표, 명령의 갯수 k
# 두번째줄부터 N개의 줄에 지도에 쓰여있는 수를 입력으로 받음

# 마지막 줄에는 명령이 순서대로 주어짐 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4

# 처음 주사위에는 전부 0이 적혀있음

# 주사위를 굴려서 한칸씩 이동시킴
# 주사위가 이동할때 어떻게 변하는지를 구현해야 함

'''
  1
3 0 2
  4
  5
'''
# 인덱스 순서대로 [위,뒤,오,왼,앞,바닥]

import sys
input = sys.stdin.readline

N,M,X,Y,K = map(int, input().split())

board = []
# 동서남북 순서대로 
dx = [0,0,-1,1]
dy = [1,-1,0,0]

dice = [0,0,0,0,0,0]

def turn(dir):
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

    if dir == 1: # 동
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    if dir == 2: # 서
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    if dir == 3: # 북
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    if dir == 4: # 남
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e

for i in range(N):
    board.append(list(map(int, input().split())))

# 명령
comm = list(map(int, input().split()))

# 주사위 좌표
nx, ny = X, Y

for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]

    # 바깥으로 이동시키려고 하는 경우
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        # 이동 취소
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    # 회전
    turn(i)

    # 이동한 칸에 쓰여있는 수가 0이면
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1] # 주사위 바닥에 적힌 숫자를 지도에 옮겨적음
    # 0이 아니면
    else:
        dice[-1] = board[nx][ny] # 칸에 쓰여있는 수가 주사위의 바닥면으로 복사됨

    print(dice[0])