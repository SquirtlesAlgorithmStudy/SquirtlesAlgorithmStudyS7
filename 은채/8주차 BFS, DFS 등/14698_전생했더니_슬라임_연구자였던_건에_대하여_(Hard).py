import sys
import heapq

T = int(sys.stdin.readline())
mod = 1_000_000_007

for _ in range(T):
    N = int(sys.stdin.readline())
    slimes = list(map(int, sys.stdin.readline().rstrip().split()))
    heapq.heapify(slimes)
    answer = 1
    
    while len(slimes) >= 2:
        min_1 = heapq.heappop(slimes)
        min_2 = heapq.heappop(slimes)
        energy = min_1 * min_2
        heapq.heappush(slimes, energy)
        answer *= energy
    
    print(answer % mod)
    
# 시간: 1032ms