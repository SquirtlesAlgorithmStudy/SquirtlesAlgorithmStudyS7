import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

R, C = map(int, input().split())  
graph = [list(input()) for _ in range(R)]  

def after_50(graph, R, C):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    new_graph = [['.'] * C for _ in range(R)] 

    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'X':  # 땅일 경우
                count_sea = 0  # 인접한 바다 수
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if ni < 0 or ni >= R or nj < 0 or nj >= C or graph[ni][nj] == '.':
                        count_sea += 1

                if count_sea < 3:  
                    new_graph[i][j] = 'X' 

    return new_graph


new_map = after_50(graph, R, C)

# 새로운 땅 크기 찾기
min_r, max_r, min_c, max_c = R, 0, C, 0

for i in range(R):
    for j in range(C):
        if new_map[i][j] == 'X':
            min_r = min(min_r, i)
            max_r = max(max_r, i)
            min_c = min(min_c, j)
            max_c = max(max_c, j)

# 지도 출력
for i in range(min_r, max_r + 1):
    print(''.join(new_map[i][min_c:max_c + 1]))