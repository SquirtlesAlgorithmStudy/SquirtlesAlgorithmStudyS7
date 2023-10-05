import sys
fastin=sys.stdin.readline().rstrip()
n = int(fastin)

from collections import deque

q = deque()
for i in range(n):
    q.append(i+1)

for i in range(n-1):
    q.popleft()
    temp = q[0]
    q.popleft()
    q.append(temp)
    
print(q[0])

#	메모리, 시간 : 31256KB	44ms