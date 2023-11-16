N,M,K =list(map(int,input().split()))
board = []
ans ={}

for _ in range(N):
       board.append(list(input()))

dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def dfs(x,y,word):
       ans[word] = ans.get(word,0)+1 
       if len(word) == 5:
              return 
       for i in range(8):
              dir_x =(x + dir[i][0])%N
              dir_y =(y + dir[i][1])%M
              dfs(dir_x,dir_y,word+board[dir_x][dir_y])

for i in range(N):
    for j in range(M):
        dfs(i, j, board[i][j])

for _ in range(K):
   print(ans.get(input().rstrip(), 0))
