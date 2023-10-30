import sys
input = sys.stdin.readline

INF = int(1e9) + 1
N = int(input())
sequence = list(map(int, input().split()))
available = list(map(int, input().split()))
operators = ["+", "-", "*", "/"]
max_val = -INF
min_val = INF


def dfs(state, accumulate, depth):
    global max_val
    global min_val
    if depth == N:
        max_val = max(accumulate, max_val)
        min_val = min(accumulate, min_val)
        return

    for i in range(4):
        if state[i] == 0:
            continue
        next_operator = operators[i]
        state[i] -= 1

        if next_operator == "+":
            dfs(state, accumulate + sequence[depth], depth + 1)
        elif next_operator == "-":
            dfs(state, accumulate - sequence[depth], depth + 1)
        elif next_operator == "*":
            dfs(state, accumulate * sequence[depth], depth + 1)
        elif next_operator == "/":
            if accumulate >= 0:
                next_val = accumulate // sequence[depth]
            else:
                next_val = -(-accumulate // sequence[depth])
            dfs(state, next_val, depth + 1)

        state[i] += 1


dfs(available, sequence[0], 1)
print(max_val)
print(min_val)
