from collections import deque

N = int(input())
d = deque([i+1 for i in range(N)])

while len(d) > 1:
    d.popleft()
    m = d.popleft()
    d.append(m)

print(d[0])
