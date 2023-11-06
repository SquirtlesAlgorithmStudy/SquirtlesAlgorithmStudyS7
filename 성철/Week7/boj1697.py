# 현재 위치가 x라면 x+1 x-1 2x로 이동 가능
# -> 방향 그래프
# 따라서 BFS로 풀 수 있다

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

time = 0
distance = [0] * 1000001

def bfs(v, k, distance):
    global time
    queue = deque()
    queue.append(v)

    
    while queue:
        now = queue.popleft()
        if now == k:
            break
        f = [now - 1, now + 1, now * 2]
            
        for i in f:
            if 0 <= i <= 100000 and distance[i] == 0:
                distance[i] = distance[now] + 1
                queue.append(i)

bfs(n, k, distance)
print(distance[k])