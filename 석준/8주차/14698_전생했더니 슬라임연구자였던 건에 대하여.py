import heapq
import sys
mod=1000000007
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    e=list(map(int, sys.stdin.readline().split()))
    ans=1
    if n==1:
        print(1)
        continue 
    q=[]
    for i in e:
        heapq.heappush(q,i)

    while len(q)!=1:
        t = heapq.heappop(q)*heapq.heappop(q)
        ans*=t
        heapq.heappush(q,t)
    print(ans%mod)