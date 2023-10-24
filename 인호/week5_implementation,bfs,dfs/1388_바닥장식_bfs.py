import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for i in range(n)]
answer = 0
for i in range(n):
    temp =''
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != temp:
                answer += 1
        temp = graph[i][j]
for i in range(m):
    temp = ''
    for j in range(n):
        if graph[j][i] =='|':
            if graph[j][i] != temp:
                answer += 1
        temp = graph[j][i]
print(answer)