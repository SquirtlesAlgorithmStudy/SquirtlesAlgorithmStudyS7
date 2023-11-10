import sys
from collections import deque
input = sys.stdin.readline

member_num = int(input())
graph = [[] for _ in range(member_num + 1)]
while True:
    edge = tuple(map(int, input().split()))
    if edge == (-1, -1):
        break
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (member_num + 1)
    result = 0
    visited[start] = True
    while q:
        member = q.popleft()
        result = max(member[1], result)
        for neighbor in graph[member[0]]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, member[1] + 1))
    return result


score_list = [member_num + 1] + ([0] * member_num)
for i in range(1, member_num + 1):
    score_list[i] = bfs(i)

candidate = []
min_score = min(score_list)
for i, score in enumerate(score_list):
    if score == min_score:
        candidate.append(i)
print(min_score, len(candidate))
print(" ".join(map(str, candidate)))

# for issue
