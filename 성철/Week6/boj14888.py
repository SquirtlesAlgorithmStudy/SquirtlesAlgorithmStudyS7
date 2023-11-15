import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

operator = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
    
    if plus:
        dfs(depth + 1, total + A[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - A[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * A[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth + 1, int(total/A[depth]), plus, minus, multiply, divide-1)

dfs(1, A[0], operator[0], operator[1], operator[2], operator[3])

print(maximum)
print(minimum)