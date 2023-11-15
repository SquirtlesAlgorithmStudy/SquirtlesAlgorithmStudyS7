from collections import deque

# N, L, R 입력 받기
N, L, R = map(int, input().split())
# 전체 나라의 인구수 정보 입력 받기
A = [list(map(int, input().split())) for _ in range(N)]

# dx,dy정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 이용해 연합을 찾고, 인구 이동이 가능한지 확인하는 함수
def process(x, y, index):
    # (x, y) 위치와 연합의 인덱스를 받아 연합을 이루는 나라들을 처리
    united = []  # 연합을 이루는 나라들의 좌표 리스트

    united.append((x, y))
    
    q = deque()
    q.append((x, y))
    union[x][y] = index  
    summary = A[x][y]  
    count = 1 
    # BFS수행
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += A[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구 분배
    for i, j in united:
        A[i][j] = summary // count
    return count

total_days = 0


while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:  
                process(i, j, index)
                index += 1

   
    if index == N * N:
        break
    total_days += 1

print(total_days)