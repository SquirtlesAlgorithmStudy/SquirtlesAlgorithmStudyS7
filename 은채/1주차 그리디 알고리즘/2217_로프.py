n = int(input())
k = []
answer = []

for i in range(n):
    k.append(int(input()))

k.sort(reverse=True)
for i in range(len(k)):
    answer.append(k[i] * (i+1))

print(max(answer))
