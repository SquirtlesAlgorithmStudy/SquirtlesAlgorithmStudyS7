import sys 

N = int(sys.stdin.readline().rstrip())
area = [[0]*100 for _ in range(100)]
answer = 0

for _ in range(N):
    i_x, i_y = sys.stdin.readline().rstrip().split(' ')
    
    for x in range(int(i_x), int(i_x)+10):
        for y in range(int(i_y), int(i_y)+10):
            area[x][y] = 1 # 색종이 부분 표시

for i in range(100):
    answer += sum(area[i]) # 색종이 부분 넓이 합
    
print(answer)