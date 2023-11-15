# N행 M열 각 칸에 알파벳이 써있고 환형으로 이어짐
# 상하좌우,대각선 8방향 이동 가능, 지나왔던 칸 재방문 허용
# 시작하는 격자의 알파벳을 시작 -> 이동할때 마다 각 칸의 알파벳을 이어붙임
# k개의 문자열이 주어짐 -> 각 문자마다 만들 수 있는 경우의 수를 구해야함
# 경우의 수를 셀 때 방문 순서가 다르면 다르다

# 1행에서 위로 가면 맨 아래 행으로 감
# 1열에서 왼쪽으로 가면 맨 오른쪽 열로 감
# 대각선 방향에 대해서도 동일한 규칙 적용

import sys 

input = sys.stdin.readline

sys.setrecursionlimit(1000000)

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]
def dfs(x, y, god, index):
    global cnt
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx == -1:
            nx = N-1
        if ny == -1:
            ny = M-1
        if nx == N:
            nx = 0
        if ny == M:
            ny = 0

        if index == len(god)-1:
            cnt += 1
            return
        else:
            
            if graph[nx][ny] == god[index+1]:
                dfs(nx, ny, god, index+1)

N, M, K = map(int, input().split())

graph = []
answer = {}
for _ in range(N):
    s = list(input().rstrip())
    graph.append(s)

for _ in range(K):
    god = list(input().rstrip())
    god_str = ''.join(god)
    cnt = 0
    if god_str in answer:
        print(answer[god_str])
    else:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == god[0]:
                    dfs(i, j, god, 0)
        answer[god_str] = cnt
        print(cnt)

