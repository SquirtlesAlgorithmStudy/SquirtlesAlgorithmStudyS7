import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

from collections import deque

N, M, K = map(int, input().split())
board = list()
for i in range(N):
  board.append(list(map(int,input().split())))

dx4 = [0,1,0,-1]
dy4 = [-1,0,1,0]
dice = [1,3,5,6,2,4]

d = 2
x, y = 0,0
score = 0

def bfs(x,y, point):
  q = deque()
  q.append((x,y))
  temp = point
  visit = [[0]* M for i in range(N)]
  visit[x][y] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx4[i]
      ny = y + dy4[i]
      if 0<=nx<N and 0<=ny<M and board[nx][ny] == point and visit[nx][ny] == 0:
        q.append((nx,ny))
        temp = temp + board[nx][ny]
        visit[nx][ny] = 1
  return temp


for i in range(K):
  # d
  x = dx4[d] + x
  y = dy4[d] + y
  if x < 0 or x >= N or y < 0 or y >= M:
    d = (d + 2) % 4
    x = dx4[d] + x
    y = dy4[d] + y
    x = dx4[d] + x
    y = dy4[d] + y

  if d == 0:
    dice = [dice[1],dice[3],dice[2], dice[5], dice[4], dice[0]]
  elif d == 1:
    dice = [dice[4],dice[1],dice[0], dice[2], dice[3], dice[5]]
  elif d == 2:
    dice = [dice[-1],dice[0],dice[2], dice[1], dice[4], dice[3]]
  elif d == 3:
    dice = [dice[2],dice[1],dice[3], dice[4], dice[0], dice[5]]

  s =  board[x][y]

  if dice[3] > s:
    d = (d - 1) % 4
  elif dice[3] < s:
    d = (d + 1) % 4
  temp = bfs(x,y,s)
  score += temp
print(score)