import sys
sys.setrecursionlimit(100000)

T = int(sys.stdin.readline().rstrip()) # 테스트 케이스 개수

def DFS (map, x, y, visited): # DFS 함수 정의
        if visited[y][x] == 0: # 방문을 하지 않았을 때만
            visited[y][x] = 1 # 방문 처리
            if y-1 >= 0:
                if map[y-1][x] == 1: # 상
                    DFS(map,x,y-1,visited)       
            if x-1 >= 0:
                if map[y][x-1] == 1: # 좌
                    DFS(map,x-1,y,visited) 
            if y+1 < int(N):   
                if map[y+1][x] == 1: # 하
                    DFS(map,x,y+1,visited)
            if x+1 < int(M):
                if map[y][x+1] == 1: # 우
                    DFS(map,x+1,y,visited)
                
for i, _ in enumerate(range(T)):
    M, N, K = list(sys.stdin.readline().rstrip().split(' '))
    cabbage_array = []
    answer = 0

    MAP = [[0]*int(M) for _ in range(int(N))] # 초기화
    visited = [[0]*int(M) for _ in range(int(N))] # 초기화
    
    for _ in range(int(K)):
        x, y = sys.stdin.readline().rstrip().split(' ')
        MAP[int(y)][int(x)] = 1 # 배추심기
        cabbage_array.append([int(x),int(y)]) # 배추 지도
    
    while len(cabbage_array) > 0: # 배추 있는 곳을 전부 확인
        x, y = cabbage_array.pop() 
        if visited[y][x] == 0: # 방문 하지 않았을 시만
            DFS(MAP,x,y,visited) # 연결된 상,하,좌,우를 전부 확인
            answer +=1 
            
    print(answer)
                