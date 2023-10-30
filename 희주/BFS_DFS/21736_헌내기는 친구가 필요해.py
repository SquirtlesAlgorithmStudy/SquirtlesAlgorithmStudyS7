import sys
from collections import deque

N, M = map(int,sys.stdin.readline().rstrip().split(' '))
MAP = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0
I_x, I_y = 0, 0 # I 의 초기 위치
queue = deque()

for index, i in enumerate(range(N)): # I 의 위치 찾기
    MAP[i] = list(sys.stdin.readline().rstrip())
    if 'I' in MAP[i]:
        I_x = index
        I_y = MAP[i].index('I')

# # print(MAP)
direction = [[1,0],[0,1],[-1,0],[0,-1]] # 하, 우, 상, 좌
visited[I_x][I_y] = 1 # 초기 위치 방문부터 시작
queue.append([I_x,I_y])

while (queue):
    x, y = queue.popleft()
    
    for dx, dy in direction:
        nx, ny = x+dx, y+dy

        # 캠퍼스를 벗어나지 않는 구역
        if 0 <= nx < N and 0 <= ny < M:
            # 벽이 아니고 방문하지 않은 곳이면 방문
            if MAP[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                
                # 사람이면 +1
                if MAP[nx][ny] == 'P':
                    answer += 1
                    
print(answer if answer > 0 else 'TT')
