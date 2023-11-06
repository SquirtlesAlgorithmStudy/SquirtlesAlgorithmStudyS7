import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque([N])
    visited[N] = 0  # 시작 위치(N)의 시간을 0으로 설정
    
    while queue:
        x = queue.popleft() # x는 시간
        if x == K: # 도착 위치(동생 위치) K에 도착 하면 시간 반환
            return visited[x]  # 최소 시간 도달
        # 3가지 방향(x-1,x+1,x*2)에 대해서 nx구하고 방문처리.
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = visited[x] + 1 # 새로운 위치 nx에서의 시간은 이전 위치 x에서 1초 경과
                queue.append(nx)
# 입력
N, K = map(int, input().split())


# 방문 여부 체크(인덱스는 위치, 값은 시간)
visited = [False] * 100001


# BFS 실행
print(bfs())