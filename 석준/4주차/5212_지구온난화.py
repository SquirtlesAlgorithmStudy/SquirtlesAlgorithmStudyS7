from sys import stdin

R, C = map(int, stdin.readline().split())

matrix = [list(input()) for _ in range(R)]

# 테두리를 포함한 배열 생성하고 모든 요소를 '.'으로 초기화
real_matrix = [['.' for _ in range(C+2)] for _ in range(R+2)]

# 기존 배열의 값을 확장된 배열에 복사
for i in range(R):
    for j in range(C):
        real_matrix[i + 1][j + 1] = matrix[i][j]

def count_adjacent(real_matrix,row, column):
    adjacent_count = []
    
    # 위쪽 원소
    
    adjacent_count.append(real_matrix[row][column+1])
       
    # 아래쪽 원소
    
    adjacent_count.append(real_matrix[row+2][column+1])
        
    # 왼쪽 원소
    
    adjacent_count.append(real_matrix[row+1][column])
      
    # 오른쪽 원소
    
    adjacent_count.append(real_matrix[row+1][column+2])
    
    
    return adjacent_count

def make_map(output_list):
    map_info = []
    for row in range(len(output_list)):
        if output_list[row].count('.') == len(output_list[0]):
            continue
        else:
            first_index = output_list[row].index('X')
            last_index = len(output_list[0]) - output_list[row][::-1].index('X') - 1
            map_info.append([row,first_index,last_index])
    return map_info

output_list = [[0] * C for _ in range(R)]

for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if matrix[row][column] == 'X':
            
            if count_adjacent(real_matrix,row, column).count('X') >=2:
                output_list[row][column] = 'X'
            else:
                output_list[row][column] = '.'
        else:
            output_list[row][column] = '.'

future_map = make_map(output_list)

if future_map == []:
    print('X')
else:
    for row in range(future_map[0][0],future_map[-1][0]+1):
        print(''.join(output_list[row][min([row[1] for row in future_map]):max([row[2] for row in future_map])+1]))
