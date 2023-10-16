import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

from collections import deque

N = int(input()) 

cards = deque(range(1, N+1))

while len(cards) > 1:  
    cards.popleft()  # 맨 위 카드 버림
    cards.append(cards.popleft())  # 그다음 카드 맨 뒤로

print(cards[0])  # 남은 카드 출력