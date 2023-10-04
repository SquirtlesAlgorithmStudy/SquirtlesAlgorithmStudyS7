from collections import deque

n = int(input())

queue = deque()

for i in range(n):
    queue.append(i+1)

while(len(queue) != 1):
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(queue[0])