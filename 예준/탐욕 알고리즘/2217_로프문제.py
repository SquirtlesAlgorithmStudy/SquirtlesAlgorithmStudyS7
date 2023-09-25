n = int(input())
rope = []
for i in range (n):
    rope.append(int(input()))

rope.sort()
value=0
for i in range(1,n+1,1):
    if (value<i*rope[n-i]):
        value = i*rope[n-i]

print(value)
