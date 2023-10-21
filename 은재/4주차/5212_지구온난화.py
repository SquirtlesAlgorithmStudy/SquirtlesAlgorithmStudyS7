r, c = map(int, input().split())

maps = [] 
for i in range(r):
    maps.append(list(input()))
    
import copy
new_maps = copy.deepcopy(maps) #50년 후의 지도

#상하좌우 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(r):
    for y in range(c):
        if maps[x][y] == '.': #바다일 경우
            continue
        
        sea_count = 0 #바다 카운트 초기화
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            #영역 밖은 바다로 취급 (지도 범위 r,c를 초과하면 바다)
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                sea_count += 1
                continue
            
            elif maps[nx][ny] == '.':
                sea_count += 1

        if sea_count >= 3: #바다가 3면 이상일 경우 바다로 변경
            new_maps[x][y] = '.'
            
start_row = 0
end_row = 0

min_index = c-1
max_index = 0

##지도 범위 구하기

#육지('X')가 존재하는 행을 찾아 start_row, end_row 설정
for i in range(r):
    if 'X' in new_maps[i]:
        start_row = i
        break

for i in range(r-1, -1, -1):
    if 'X' in new_maps[i]:
        end_row = i
        break

#육지가 존재하는 행에서의 최소/최대 인덱스 탐색
for i in range(start_row, end_row+1):
    tmp = [i for i, value in enumerate(new_maps[i]) if value == 'X']
    
    if not tmp: #현재 행에 'X'가 없을 시 다음 행 탐색
        continue
    
    min_tmp = tmp[0] #인덱스 중 가장 작은 값을 min_tmp로 할당
    max_tmp = tmp[-1] #인덱스 중 가장 큰 값을 min_tmp로 할당
    min_index = min(min_index, min_tmp) #이전 인덱스와 현재 인덱스 중 더 작은 값 할당
    max_index = max(max_index, max_tmp) #이전 인덱스와 현재 인덱스 중 더 큰 값 할당

#정답 출력
for i in range(start_row, end_row+1):
    for j in range(min_index, max_index+1):
        print(new_maps[i][j], end='')
    print()