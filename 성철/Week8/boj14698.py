import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    slime = list(map(int, input().split()))
    energy = 1

    # slime 리스트를 최소 힙으로 변환
    heapq.heapify(slime)

    while len(slime) > 1:
        a = heapq.heappop(slime)
        b = heapq.heappop(slime)
        comp = a*b

        energy *= comp
        heapq.heappush(slime, comp)

    print(energy%1000000007)

