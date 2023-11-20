import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

N, atk = map(int,input().split())
rooms = []
# 어차피 rooms별로 진행해야 하므로 나중에 추가
HP = 0 
HPcur = 0 
dam = 0

# 방 돌아다니기
for i in range(N):
    rooms.append(list(map(int,input().split())))

    if rooms[i][0] == 1: 
        temp = rooms[i][2] % atk
        if temp == 0:
            dam = -(rooms[i][1] * (rooms[i][2] // atk -1))
        else:
            dam = -(rooms[i][1] * (rooms[i][2] // atk))

    else: 
        dam = rooms[i][2] 
        atk += rooms[i][1] 

    HPcur += dam

    if HPcur > 0 :
        HPcur = 0 
    
    HP = max(HP,abs(HPcur))

print(HP+1)