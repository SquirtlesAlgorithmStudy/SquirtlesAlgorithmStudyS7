white = [[0 for _ in range(100)] for _ in range(100)]
color_num = int(input())
color_position = []
black = 0

for i in range(color_num):
    color_position.append(list(map(int, input().split())))

for position in color_position:
    for i in range(10):
        for j in range(10):
            white[position[0]-1+i][position[1]-1+j] = 1

for x in range(100):
    for y in range(100):
        if(white[x][y]==1):
            black += 1

print(black)