import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())


graph = []
visited= [[False] * M for _ in range(N)]
for _ in range(N):
    s = list(map(int, input().split()))
    graph.append(s)

dice = [1,2,3,4,5,6] # 위뒤오왼앞바닥

def turn(dir):
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

    if dir == 0: # 동
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    if dir == 2: # 서
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    if dir == 3: # 북
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    if dir == 1: # 남
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e

# 처음 이동 방향은 동쪽, 시작점은 1,1
# 이동 방향으로 한 칸 굴러감, 이동 방향에 칸이 없다면(그래프 밖이라면) 반대로 한칸 굴림
# 도착한 칸에 대한 점수 획득
# 주사위 아랫면(dice[5])와 주사위가 있는 칸 x,y에 있는 정수 b를 비교해 이동 방향 결정
## A > B인 경우 이동 방향을 시계 방향으로 90도 회전, A < B인 경우 90도 반시계 A=B인 경우 그대로
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 0

def dfs(x,y):
    visited[x][y] = True
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] == graph[x][y]:
                if visited[nx][ny] == False:
                
                    dfs(nx, ny)

# 현재 위치
cur_x = 0
cur_y = 0
rotate = 0 # 최초 이동 방향 : 동쪽

score = 0

for _ in range(K):
    # 주사위 이동 - 그래프를 벗어난 경우 예외처리 해줘야함
    nx = cur_x + dx[rotate]
    ny = cur_y + dy[rotate]
    
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        rotate = (rotate+2) % 4
        nx = cur_x + dx[rotate]
        ny = cur_y + dy[rotate]
    turn(rotate)
    # visited 배열 초기화
    cur_x = nx
    cur_y = ny
    visited= [[False] * M for _ in range(N)]
    cnt = 0
    dfs(cur_x, cur_y)
    
    score += (cnt * graph[cur_x][cur_y])

    # 다음 주사위 이동 방향 결정
    if dice[5] > graph[cur_x][cur_y]:
        rotate = (rotate+1)%4
    elif dice[5] < graph[cur_x][cur_y]:
        rotate = (rotate-1)%4
        if rotate == -1:
            rotate = 3
    
    
    
print(score)