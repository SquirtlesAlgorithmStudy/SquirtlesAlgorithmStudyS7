n = int(input())

from collections import deque

card = deque()

#카드 생성
for i in range(1,n+1):
    card.append(i)
    
while len(card)>1:
    card.popleft()
    a=card[0]
    card.append(a)
    card.popleft()
    
print(card.popleft())