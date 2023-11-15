import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

# 보드 크기 입력
N = int(input())
# 사과의 갯수 입력
len_A = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]


# 사괴의 위치 입력
for _ in range(len_A):
    a, b = map(int, input().split())
    graph[a][b] = 1 # 사과 위치는 1로

L = int(input())
move = []

# 뱀 움직임 입력
for _ in range(L):
    X, C = input().split()
    move.append((int(X), C))

# 뱀 방향 (오른쪽, 아래쪽, 왼쪽, 위쪽)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 1, 1 # 뱀의 초기 위치
graph[x][y] = 2 # 뱀이 있는 위치는 2로
direction = 0 # 시작은 오른쪽 (0부터 3까지 오,아,왼,위)
time = 0 # 소요시간
index = 0 # 회전 정보 인덱스
tail = [(x,y)] # 뱀 위치 정보 (꼬리가 맨 첫 번째에 있게끔 스택 형식으로 쌓음)

while True:
    # break 전까지 direction에 맞게 nx, ny 이동
    nx, ny = x + dx[direction], y + dy[direction]
    # 맵 안에 있는지 확인하고, 뱀이 뱀이랑 마주쳐서 죽는지 확인하기
    if 1 <= nx <= N and 1 <= ny <= N and graph[nx][ny] != 2:
        # 사과가 없는 곳(0)을 방문하는 경우
        if graph[nx][ny] == 0 :
            # 새로운 몸통위치를 입력(2)
            graph[nx][ny] = 2
            # 꼬리 리스트(tail)에 입력
            tail.append((nx,ny))
            # 사과를 안먹었으니, 꼬리를 짤라야 함
            px, py = tail.pop(0) 
            graph[px][py] = 0
        # 사과가 있는 곳(1)을 방문하는 경우
        if graph[nx][ny] == 1:
            graph[nx][ny] = 2
            # 그냥 꼬리 하나 스택형식으로 쌓으면 된다~
            tail.append((nx,ny))
    else: # break 조건
        time += 1 # 이거 추가안해서 왜틀렸나 한참 찾았다. 부딪히는데 1초를 추가해야 함.
        break
    # 이동 한번 마쳤으니 그 다음번 이동을 위해 세팅
    x, y = nx,ny
    time += 1
    # 회전하는 거는 index를 선형탐색 하는 식으로 
    if index < L and time == move[index][0]:
        if move[index][1] == 'L':
            direction = (direction -1) % 4
        else:
            direction = (direction + 1) % 4
        index += 1
print(time)