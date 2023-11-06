import sys
sys.setrecursionlimit(100000) # 재귀 

N, M = sys.stdin.readline().rstrip().split(' ') # 세로, 가로
FLOOR = [[0]*int(M) for _ in range(int(N))] # 바닥 장식 맵
visited = [[0]*int(M) for _ in range(int(N))] # 방문 지도 
answer = 0 # 정답

for j in range(int(N)): # 바닥 장식 맵 그리기 
    FLOOR[j] = list(sys.stdin.readline().rstrip())

def down(m,n,visited): # | 일 때 아래로 확인하는 함수 
    if m < int(M) and n < int(N):
        if visited[n][m] == 0: # 방문하지 않았을 때만
            if FLOOR[n][m] == '|': 
                visited[n][m] = 1 
                down(m,n+1,visited) # 계속 아래로 확인
      
def right(m,n,visited): # - 일때 가로로 확인하는 함수
    if m < int(M) and n < int(N):
        if visited[n][m] == 0: # 방문하지 않았을 때만
            if FLOOR[n][m] == '-':
                visited[n][m] = 1
                right(m+1,n,visited) # 계속 옆으로 확인

for n in range(int(N)): # 세로
    for m in range(int(M)): # 가로
        if visited[n][m] == 0: # 방문하지 않았을 때만
            visited[n][m] = 1 
            if FLOOR[n][m] == '-': # - 면 오른쪽 옆으로 확인
                right(m+1,n,visited)
                answer += 1 
                
            elif FLOOR[n][m] == '|': # | 면 바로 아래로 확인
                down(m,n+1,visited)
                answer += 1
            
print(answer)