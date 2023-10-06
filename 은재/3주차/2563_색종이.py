n = int(input())
paper = [[0] * 100 for _ in range(100)] #100x100 도화지 생성

for _ in range(n):
    w, h = map(int, input().split()) #넓이, 높이 입력받기
    
    for i in range(w, w+10): 
        for j in range(h, h+10):
            paper[i][j] = 1 #픽셀값 0>1 로 변경
            
cnt = 0
for i in paper:
    cnt += sum(i) #픽셀값 더해주기
            
print(cnt)