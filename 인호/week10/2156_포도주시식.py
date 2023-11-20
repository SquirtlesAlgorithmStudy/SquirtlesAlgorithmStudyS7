import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for _ in range(n)]
d = [0] * n

d[0] = graph[0]

if n > 1:
    d[1] = graph[0] + graph[1]

if n > 2:
    d[2] = max(graph[0] + graph[2], graph[1] + graph[2], d[1])


for i in range(3, n):
    d[i] = max(d[i - 1], d[i - 3] + graph[i - 1] + graph[i], d[i - 2] + graph[i])

print(max(d))