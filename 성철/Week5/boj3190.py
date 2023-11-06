import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
    X, Y = map(int, input().split())
    graph[X-1][Y-1] = 1

L = int(input())

# 이동 방향 -> 처음에는 오른쪽을 향함
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 회전 관련 내용을 저장할 list
turn = []

for _ in range(L):
    X, Y = map(str, input().rstrip().split())
    turn.append((int(X), Y))


snake = deque([(0,0)])
head_x = 0
head_y = 0
direction = 0
direction_index = 0
time = 0
print(turn)
while 1:
    head_x = head_x + dx[direction]
    head_y = head_y + dy[direction]

    time += 1

    if head_x < 0 or head_x >= N or head_y < 0 or head_y >= N or (head_x,head_y) in snake:
        break
    
    snake.append((head_x,head_y))
    print(snake)
    if graph[head_x][head_y] == 0:
        snake.popleft()
    else:
        graph[head_x][head_y] = 0
    if time == turn[direction_index][0]:
        if turn[direction_index][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        
        if direction_index + 1 < len(turn):
            direction_index += 1

print(time)

