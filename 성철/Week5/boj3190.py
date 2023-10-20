import sys
input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
    X, Y = map(int, input().split())
    graph[X-1][Y-1] = 1

L = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

rotation_time = []
rotation = []

for _ in range(L):
    X, Y = map(str, input().rstrip().split())
    rotation_time.append(int(X))
    rotation.append(Y)

snake = [(0,0)]

