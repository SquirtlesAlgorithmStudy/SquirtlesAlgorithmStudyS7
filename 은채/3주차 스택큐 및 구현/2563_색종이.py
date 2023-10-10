N = int(input())
drawing_paper = [[0] * 100 for i in range(100)]
result = 0

for i in range(N):
    x, y = map(int, input().split())

    for j in range(x, x + 10):
        for k in range(y, y + 10):
            drawing_paper[j][k] = 1

for i in range(100):
    result += sum(drawing_paper[i])

print(result)
