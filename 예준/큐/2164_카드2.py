import sys
fastin=sys.stdin.readline().rstrip()

n = int(fastin) # N 입력받기

from collections import deque

q = deque()

for i in range(n): # 초기세팅
    q.append(i+1)

for i in range(n-1): # N-1번 시행
    # 맨 윗 카드 제거
    q.popleft() 
    # 제일 위에 있는 카드 저장
    temp = q[0]
    # 제일 아래로 이동 
    q.popleft()
    q.append(temp) 

# 남은 카드 번호 출력
print(q[0])

#	메모리, 시간 : 	51044KB	216ms