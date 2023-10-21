import sys 
import heapq

H, W = sys.stdin.readline().rstrip().split(' ')
MAP =[[0]*(int(W)+2) for _ in range(int(H)+2)]
result = [[0]*(int(W)+2) for _ in range(int(H)+2)]

# 초기화
for i in range(1, int(H)+1):
    map = sys.stdin.readline().rstrip()
    j = 1
    for m in map:
        if m == '.':
            MAP[i][j] = 0
            result[i][j] = 0
        else:
            MAP[i][j] = 1
            result[i][j] = 1
        j += 1

for i in range(1, int(H)+1):
    for j in range(1, int(W)+1):
        if MAP[i][j] == 1:
            count = 0
            count += MAP[i][j-1] + MAP[i-1][j] + MAP[i][j+1] + MAP[i+1][j]
            if count <= 1:
                result[i][j] = 0

# 자를 테두리 인덱스 구하기
I_s, I_f, J_s, J_f = 0, 0, 0, 0
for i_s in range(int(H)+2):
    if sum(result[i_s]) == 0:
        pass
    else:
        I_s = i_s
        break
for i_f in range(int(H)+1, -1, -1):
    if sum(result[i_f]) == 0:
        pass
    else:
        I_f = i_f
        break 
for j_s in range(int(W)+2):
    if sum(row[j_s] for row in result) == 0:
        pass
    else:
        J_s = j_s
        break
for j_f in range(int(W)+1, -1, -1):
    if sum(row[j_f] for row in result) == 0:
        pass
    else:
        J_f = j_f
        break
    
# 슬라이싱
result = [row[J_s:J_f+1] for row in result[I_s:I_f+1]]
# print(result)

# 이진 값을 변환
for row in result:
    answer = ''
    for r in row:
        if r == 0:
            answer += '.'
        else:
            answer += 'X'
    print(answer)