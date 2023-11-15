import sys

N = sys.stdin.readline().rstrip()
NUMBERS= list(map(int,sys.stdin.readline().rstrip().split(' ')))
OPERATORS = list(map(int,sys.stdin.readline().rstrip().split(' ')))

# print(N, NUMBERS , OPERATORS)

#DFS
def dfs(numbers, operators):
    if len(numbers) == 1:
        # return 최대값, 최소값
        return numbers[0], numbers[0]

    min_n = float('inf')
    max_n = float('-inf')
    
    for i in range(4):
        if operators[i] != 0:
            operators[i] -= 1
            if i == 0: # 덧셈 개수
                cur_max, cur_min = dfs([numbers[0] + numbers[1]] + numbers[2:], operators)
            elif i == 1: # 뺼셈 개수
                cur_max, cur_min = dfs([numbers[0] - numbers[1]] + numbers[2:], operators)
            elif i == 2: # 곱셈  개수
                cur_max, cur_min = dfs([numbers[0] * numbers[1]] + numbers[2:], operators)
            else: # 나눗셈 개수
                num = -(-numbers[0] // numbers[1]) if numbers[0] < 0 else numbers[0] // numbers[1]
                cur_max, cur_min = dfs([num] + numbers[2:], operators)
            
            operators[i] += 1
            min_n = min(min_n, cur_min)
            max_n = max(max_n, cur_max)
            
    return max_n, min_n

max, min = dfs(NUMBERS, OPERATORS)
print(max)
print(min)