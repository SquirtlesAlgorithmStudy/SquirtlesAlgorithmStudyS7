import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

from collections import deque
import sys

T = int(input())

# bfs 함수 정의
def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # break 조건
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 배추가 심어져 있을 때
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 해당 배추 위치 방문 처리
                queue.append((nx, ny))  # 다음 위치를 큐에 삽입

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    #BFS 수행
    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:  # 배추가 있으면 BFS
                bfs(i, j)
                result += 1  # 지렁이 증가

    # 지렁이 수 출력
    print(result)