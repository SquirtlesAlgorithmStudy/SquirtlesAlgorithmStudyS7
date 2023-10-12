# 백준 지구온난화

import sys
import copy
input = sys.stdin.readline

# 지도 크기 입력받음
R,C = map(int, input().split())
# 지도 입력 받음

map_ = []
for _ in range(R):
    line = list(input().rstrip())
    map_.append(line)

result = copy.deepcopy(map_)

# 순회 돌면서 +-1 구간에서 인접한 곳의 바다를 세서 3 이하면 새로운 배열에서 체크해줌

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for y in range(R):
    for x in range(C):
        # 바다인 경우
        if map_[y][x] == '.':
            continue
        count = 0
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]

            if 0 <= ny < R and 0 <= nx < C:
                if map_[ny][nx] == '.':
                    count += 1
            else: # 지도 바깥
                count += 1
        
        if count >= 3:
            result[y][x] = '.'
            # 원본은 가만히 두고 deepcopy된 지도를 수정해줘야함

# 테두리를 어떻게 없앨것인가?

# X가 나오는 행을 찾아서 list에 저장
X_row = []
for i in range(R):
    if 'X' in result[i]:
        X_row.append(i)

# X가 나오는 열을 찾아서 list에 저장 
X_column = []

for j in range(C):
    for i in range(X_row[0], X_row[-1]+1):
        if result[i][j] == 'X':
            X_column.append(j)
            break

for i in range(X_row[0], X_row[-1]+1):
    print(''.join(result[i][X_column[0]:X_column[-1]+1]))
