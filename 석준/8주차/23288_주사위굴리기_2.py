from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 이거 쓰면 틀렸다고 나옴 왜 그러지??
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# if dice[5] > graph[row][column]:
#         dir = (dir + 1) % 4
#     elif dice[5] < graph[row][column]:
#         dir = (dir + 3) % 4
# 이 부분에서 시계, 반시계 방향이 다르게 정의되어있어서 오류가 발생한다고 한다!!!

dice = [1, 2, 3, 4, 5, 6]
row, column = 0,0
result = 0
dir = 0
# 동 -> 4 2 1 6 5 3
# 서 -> 3 2 6 1 5 4
# 북 -> 5 1 3 4 6 2
# 남 -> 2 6 3 4 1 5
# 시계 -> 1 4 2 3 5 6
# 반시계 -> 1 3 5 4 2 6


def bfs(i, j, B):
    queue = deque()
    visited[i][j] = 1
    union = 1
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if graph[nx][ny] == B:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union += 1
    return union

for _ in range(K):

    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    # 주사위의 위치가 맵 끝에 도달한 경우
    if row + dx[dir] < 0 or column + dy[dir] < 0 or row + dx[dir]  >= N or column + dy[dir] >= M:
        dir = (dir + 2) % 4
    
    row,column = row + dx[dir], column + dy[dir]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    # 주사위가 도착한 칸에 대한 점수
    B = graph[row][column]
    # 연속해서 이동할 수 있는 칸의 수
    C = bfs(row, column, B)
    result += B*C
    # 동쪽이동
    if dir == 0:
        dice = [d, b, a, f, e, c]
    # 남쪽이동
    elif dir == 1:
        dice = [b, f, c, d, a, e]
    # 서쪽이동
    elif dir == 2:
        dice = [c, b, f, a, e, d]
    # 북쪽이동
    else:
        dice = [e, a, c, d, f, b]

    if dice[5] > graph[row][column]:
        dir = (dir + 1) % 4
    elif dice[5] < graph[row][column]:
        dir = (dir + 3) % 4
        
print(result)

