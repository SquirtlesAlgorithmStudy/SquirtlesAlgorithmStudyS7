import sys

infos= list(map(int,sys.stdin.readline().rstrip().split()))
map_=[]
direction=[(1,0),(-1,0),(0,1),(0,-1)]
dice=[[0],[0,0,0],[0],[0]]
dice_bottom=0
start=[infos[1],infos[2]]
result=[]

for N in range(infos[0]):
    num=list(map(int,sys.stdin.readline().rstrip().split()))
    map_.append(num)

commands=list(map(int,sys.stdin.readline().split()))
for command in commands:
    dx,dy=direction[command+1]
    if 0>start[0]+dx and start[0]>=infos[0]:
        continue
    elif 0>start[1]+dy and start[1]>=infos[1]:
        continue
    else:
        start[0]+=dx
        start[1]+=dy
    if map_[start[0]][start[1]]==0:
        
        