import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    slimes = list(map(int, input().split()))
    heapq.heapify(slimes)

    answer = 1

    while len(slimes) > 1:
        first_slime = heapq.heappop(slimes)
        second_slime = heapq.heappop(slimes)
        new_slime = first_slime * second_slime
        answer *= new_slime
        heapq.heappush(slimes, new_slime)

    print(answer % 1_000_000_007)
