import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
string_list = [input().rstrip() for _ in range(K)]

dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, -1, 1, -1, 1]
string_dict = {}
max_len = 0
for item in string_list:
    string_dict[item] = 0
    max_len = max(max_len, len(item))


def dfs(r, c, s):
    for i in range(8):
        nr = (r + dr[i]) % N
        nc = (c + dc[i]) % M
        new_s = s + board[nr][nc]
        if string_dict.get(new_s) is not None:
            string_dict[new_s] += 1
        if len(new_s) < max_len:
            dfs(nr, nc, new_s)


if max_len == 1:
    flag = False
else:
    flag = True

for i in range(N):
    for j in range(M):
        if string_dict.get(board[i][j]) is not None:
            string_dict[board[i][j]] += 1
        if flag:
            dfs(i, j, board[i][j])

for item in string_list:
    print(string_dict[item])
