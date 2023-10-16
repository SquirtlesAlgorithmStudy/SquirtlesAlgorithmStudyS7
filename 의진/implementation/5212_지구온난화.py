import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
number_representation = deque([0] for _ in range(R))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

left_min = 11
right_min = 11

for idx_r, row in enumerate(board):
    for idx_c, point in enumerate(row):
        if point == ".":
            number_representation[idx_r][-1] += 1
        else:
            count_island = 0
            for i in range(4):
                nr = idx_r + dr[i]
                nc = idx_c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == "X":
                    count_island += 1
                    if count_island == 2:
                        break
            if count_island == 2:
                number_representation[idx_r].append(0)
            else:
                number_representation[idx_r][-1] += 1
    left_min = min(left_min, number_representation[idx_r][0])
    right_min = min(right_min, number_representation[idx_r][-1])

while len(number_representation[0]) == 1:
    number_representation.popleft()
while len(number_representation[-1]) == 1:
    number_representation.pop()
for row in number_representation:
    if len(row) == 1:
        print("." * (row[0] - left_min - right_min))
    else:
        result = ""
        result += ("." * (row[0] - left_min))
        for item in row[1:-1]:
            result += "X"
            result += ("." * item)
        result += "X"
        result += ("." * (row[-1] - right_min))
        print(result)

# Finish
