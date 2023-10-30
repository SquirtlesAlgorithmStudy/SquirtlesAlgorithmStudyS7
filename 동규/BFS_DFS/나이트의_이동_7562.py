import sys
from collections import deque

nums = int(input())
directions=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
result=[]
def dfs(start,graph,target):
    queue=deque([start])
    graph[start[0]][start[1]]=1
    while queue:
        R,C=queue.popleft()
        for direction in directions:
            if R+direction[0]<0 or C+direction[1]<0:
                continue
            elif R+direction[0]>=len(graph) or C+direction[1]>=len(graph):
                continue  
            elif graph[R+direction[0]][C+direction[1]]==0:
                graph[R+direction[0]][C+direction[1]]=graph[R][C]+1
                queue.append((R+direction[0],C+direction[1]))
        if graph[target[0]][target[1]]!=0:
            break
    return graph[target[0]][target[1]]-1

for num in range(nums):
    for i in range(3):
        if i%3==0:
            board=int(sys.stdin.readline().rstrip())
            chess_board=[[0]*board for i in range(board)]
        elif i%3==1:
            start_R,start_C = map(int,sys.stdin.readline().split())
            start=(start_R,start_C)
        elif i%3==2:
            target_R,target_C=map(int,sys.stdin.readline().split())
            target=(target_R,target_C)
    result.append(dfs(start,chess_board,target))

for i in range(len(result)):
    print(result[i])