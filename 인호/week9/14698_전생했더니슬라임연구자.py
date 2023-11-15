import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

import heapq

for _ in range(int(input())):
    input()
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    ans = 1
    while len(heap) > 1:
        a = heapq.heappop(heap) * heapq.heappop(heap)
        ans *= a
        heapq.heappush(heap, a)
    print(ans % 1000000007)