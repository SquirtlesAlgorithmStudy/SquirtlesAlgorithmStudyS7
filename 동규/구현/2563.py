import sys

papers = int(input())
big_paper=[[0]*100 for i in range(100)]
num_count=0

for paper in range(papers):
    W,H = map(int, sys.stdin.readline().split())
    for width in range(W,W+10):
        for height in range(H,H+10):
            big_paper[width][height]+=1
for i in range(100):
    for j in range(100):
        if big_paper[i][j]!=0:
            num_count+=1
print(num_count)

        