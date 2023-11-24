import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dijkstra(start_i, start_j, end_i, end_j):
    global N
    hq = []
    heapq.heappush(hq, (board[start_i][start_j], (start_i, start_j)))
    dp[start_i][start_j] = board[start_i][start_j]

    while hq:
        dist, now = heapq.heappop(hq)
        if visited[now[0]][now[1]]:
            continue
        visited[now[0]][now[1]] = True

        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc]:
                    continue
                cost = dp[now[0]][now[1]] + board[nr][nc]
                dp[nr][nc] = min(dp[nr][nc], cost)
                heapq.heappush(hq, (cost, (nr, nc)))

    return dp[end_i][end_j]


t = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[INF] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = dijkstra(0, 0, N-1, N-1)
    print(f"Problem {t}: {result}")
    t += 1
