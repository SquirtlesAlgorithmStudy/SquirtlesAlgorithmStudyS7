n = int(input())
location = [list(map(int, input().split())) for _ in range(n)]

board = [[0 for j in range(100)] for i in range(100)]
area = 0 
for k in range(n):
    x = location[k][0]
    y = location[k][1]
    for i in range(10):
        for j in range(10):
            if(board[x+i][y+j]) == 0:
                board[x+i][y+j] = 1
                area += 1    
print(area)