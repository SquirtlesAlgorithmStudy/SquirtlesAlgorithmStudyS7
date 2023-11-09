from collections import deque

N, K = map(int, input().split())


def bfs(s):
    queue = deque()
    queue.append(s)
    graph[s] = 1

    while queue:
        s = queue.popleft()

        if s == K:
            return graph[s] - 1

        for ns in [s-1, s+1, s*2]:
            if ns < 0 or ns > 100000:
                continue
            if graph[ns] == 0:
                graph[ns] = graph[s] + 1
                queue.append(ns)


graph = [0 for _ in range(100001)]

print(bfs(N))

# 시간: 100ms
