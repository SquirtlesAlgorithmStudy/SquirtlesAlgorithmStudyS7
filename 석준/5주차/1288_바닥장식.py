import sys
sys.setrecursionlimit(10**6)
room_bottom = []
count = 0
row,col = map(int, input().split())
for i in range(row):
    room_bottom.append(list(input()))
    
def dfs(x,y):

    global count
    
    if x<= -1 or x>= len(room_bottom) or y<= -1 or y >=len(room_bottom[0]):
        return False
    if room_bottom[x][y] == '-':

        room_bottom[x][y] = count

        # dfs(x,y-1)
        if y+1 >= len(room_bottom[0]) or room_bottom[x][y+1] == '|':
            return True
        else:
            dfs(x,y+1)
            count += 1
            return True
    
    if room_bottom[x][y] == '|':

        room_bottom[x][y] = count

        # dfs(x-1,y)
        if x+1 >= len(room_bottom) or room_bottom[x+1][y] == '-':
            return True
        else:
            dfs(x+1,y)
            count += 1
            return True
    
    return False

result = 0
n,m = len(room_bottom),len(room_bottom[0])
for i in range(n):
    for j in range(m):

        if dfs(i,j) == True:
            result += 1

print(result)