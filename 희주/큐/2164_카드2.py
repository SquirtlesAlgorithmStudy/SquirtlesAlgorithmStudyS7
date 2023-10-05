import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) # 카드 갯수
queue = deque([(n+1) for n in range(N)]) # 1부터 N까지 리스트 생성

while len(queue) > 2: # queue가 2개 이상일 때
    queue.popleft() # 제일 위에 있는 카드 버림
    queue.append(queue.popleft()) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다

if len(queue) == 2: # queue가 2장 일때
    queue.popleft() # 앞장은 버림

print(queue.popleft()) # 남은 card 출력