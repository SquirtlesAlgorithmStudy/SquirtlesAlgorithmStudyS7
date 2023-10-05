import sys
from collections import deque

cards = int(sys.stdin.readline())
card_list=[]

for card in range(1,cards+1):
    card_list.append(card)
card_list=deque(card_list)
while True:
    if len(card_list)==1:
        break
    card_list.popleft()
    card_list.append(card_list.popleft())

print(card_list[0])