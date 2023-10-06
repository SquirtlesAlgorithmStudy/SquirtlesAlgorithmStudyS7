from collections import deque

N = int(input())
deque_ = deque([i for i in range(1,N + 1)])

while len(deque_) > 1:
    deque_.popleft()
    deque_.append(deque_.popleft())

print(deque_[0])