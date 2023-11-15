import sys
import copy
R,C= map(int,sys.stdin.readline().split())
jido=[list(sys.stdin.readline().strip()) for row in range(R)]
copy_jido=copy.deepcopy(jido)
count=0
direction=[[1,0],[-1,0],[0,-1],[0,1]]

for row in range(R):
    for col in range(C):
        if jido[row][col]=="X":
            for dir in direction:
                if row+dir[0]<0 or col+dir[1]<0:
                    count+=1
                    continue
                elif row+dir[0]==R or col+dir[1]==C:
                    count+=1
                    continue
                if jido[row+dir[0]][col+dir[1]]==".":
                    count+=1
            if count>=3:
                copy_jido[row][col]="."
                count=0
            else:
                count=0

print(''.join(map(str,jido[1][1:8])))
min_x,max_x,min_y,max_y=0,0,0,0


