R, C = list(map(int, input().split()))
map = []
delete_land = []
land_r = []
land_c = []

for r in range(R):
    map.append(list(input()))
    for c in range(C):
        if(map[r][c] == 'X'):       # 땅이 있는 곳 위치 저장
            land_r.append(r)
            land_c.append(c)
            
def detection_sea(r,c):
    sea = 0
    if(c==0):                       # 맨 왼쪽에 땅이 있을 때(모서리 제외)
        if(r != 0 and r != R-1):
            if(map[r+1][c] == '.'):
                sea += 1
            if(map[r-1][c] == '.'):
                sea += 1
            if(c+1<=C-1 and map[r][c+1] == '.'):
                sea += 1
            if(sea == 3):
                delete_land.append([r,c])
    elif(c==C-1):                    # 맨 오른쪽에 땅이 있을 때
        if(r != 0 and r != R-1):
            if(map[r+1][c] == '.'):
                sea += 1
            if(map[r-1][c] == '.'):
                sea += 1
            if(c-1>=0 and map[r][c-1] == '.'):
                sea += 1
            if(sea == 3):
                delete_land.append([r,c])
    elif(r==0):
        if(c != 0 and c != C-1):       # 맨 위쪽에 땅이 있을 때
            if(map[r][c+1] == '.'):
                sea += 1
            if(map[r][c-1] == '.'):
                sea += 1
            if(r+1<=R-1 and map[r+1][c] == '.'):
                sea += 1
            if(sea == 3):
                delete_land.append([r,c])
    elif(r==R-1):
        if(c != 0 and c != C-1):       # 맨 아래쪽에 땅이 있을 때
            if(map[r][c+1] == '.'):
                sea += 1
            if(map[r][c-1] == '.'):
                sea += 1
            if(r-1>=0 and map[r-1][c] == '.'):
                sea += 1
            if(sea == 3):
                delete_land.append([r,c])
    else:                             # 지도의 가장자리가 아닐 떄
        if(map[r-1][c] == '.'):
            sea += 1
        if(map[r+1][c] == '.'):
            sea += 1
        if(map[r][c-1] == '.'):
            sea += 1
        if(map[r][c+1] == '.'):
            sea += 1
        if(sea >= 3):
            delete_land.append([r,c])

for k in range(len(land_r)):       # 땅의 이웃한 삼면 이상이 바다인지 확인
    detection_sea(land_r[k], land_c[k])

for r, c in delete_land:           # 땅 -> 바다
    map[r][c] = '.'


# 가장 작은 직사각형 만들기
# 가장자리에 'X' 존재하는지 찾기  
while(1):
    if(C>1 and R>1):
        if((map[0].count('X') != 0) and (map[-1].count('X') != 0) and (map[:][0].count('X') != 0) and (map[:][-1].count('X') != 0)):
            break
        elif(map[0].count('.') == C):        # 맨 윗줄 모두 바다
            map[0].clear()
            R -= 1
        elif(map[-1].count('.') == C):        # 맨 아랫줄 모두 바다
            map[-1].clear()
            R -= 1
        elif(map[:][0].count('.') == R):     # 맨 왼쪽 모두 바다
            map[:][0].claer()
            C -= 1
        elif(map[:][-1].count('.') == R):      # 맨 오른쪽 모두 바다
            map[:][-1].clear()
            C -= 1
    else: break


# 결과 출력
if (map.count('X') == 0):
    print('X')
else:
    for r in range(R):
        print(''.join(map[r]))