import sys
import heapq
Ts = int(input())
results=[]
for T in range(Ts):
    N=int(sys.stdin.readline().rstrip())
    C_i=list(map(int,sys.stdin.readline().rstrip().split()))
    if N==1:
        results.append(N)
        continue
    heapq.heapify(C_i)
    result=1
    while len(C_i)!=1:
        
        S_one=heapq.heappop(C_i)
        S_two=heapq.heappop(C_i)
        
        S=S_one*S_two
        

        heapq.heappush(C_i,S)
        result=(result*S)%1000000007

    results.append(result)

for result in results:
    print(result)