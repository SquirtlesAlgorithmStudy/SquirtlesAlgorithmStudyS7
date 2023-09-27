import sys

input = sys.stdin.readline
N = int(input())
cards = [i for i in range(1, N+1)]

def solution_using_queue(cards):
    while len(cards) > 1:
        cards.pop(0)
        cards.append(cards.pop(0))
    return cards[0]

def solution(cards):
    while len(cards) > 1:
        n = len(cards)
        cards = cards[1::2]
        if n % 2 == 1:
            cards.append(cards.pop(0))
    return cards[0]

print(solution(cards))
for i in range(2, 11):
    cards = [i for i in range(1, i)]
    print(i - 1, solution(cards))