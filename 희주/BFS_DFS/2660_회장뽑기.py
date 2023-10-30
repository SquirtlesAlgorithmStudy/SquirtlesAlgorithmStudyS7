import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
relation_map = [[0]*N for _ in range(N)]

while True:
    member_1, member_2 = map(int,sys.stdin.readline().rstrip().split(' ')) # 둘은 친구 사이 
    
    if member_1 == -1 and member_2 == -1: # 입력 종료 조건
        break
    else:
        relation_map[member_1-1][member_2-1] = 1 
        relation_map[member_2-1][member_1-1] = 1 # 양방향

#BFS
def BFS(start):
    # 각 멤버별 다른 멤버까지의 최단거리를 나타내는 visited
    visited[start] = 0 # 시작점
    queue = deque([[start, 0]])
    
    while queue: # 반복
        cur, n = queue.popleft()
        for i in range(N): 
            if relation_map[cur][i] == 1 and visited[i] == -1: # 친구이면서, 방문하지 않은 멤버
                visited[i] = n + 1 # start부터 i까지의 점수 (최단거리 길이)
                queue.append([i,n+1]) # [현재 정점,현재 정점까지 최단거리]

# 각 후보자의 최대 친구 관계
member_dict = {}
for i in range(N):
    visited = [-1] * N # 각 후보별 다른 후보와의 최단 거리 수 
    BFS(i)
    member_dict[i] = max(visited) # 최단 거리 중 가장 긴 거리가 각 후보의 점수가 된다

score = min(member_dict.values()) # 가장 작은 값이 회장 후보 점수
candidate_list = [ str(k+1) for k, v in member_dict.items() if v == score] # 회장의 후보 리스트
print(score, len(candidate_list)) # 회장 후보의 점수, 회장 후보의 수 
print(' '.join(candidate_list)) # 회장 후보 리스트 출력

## 18352 특정거리도시찾기와 비교
# 단방향