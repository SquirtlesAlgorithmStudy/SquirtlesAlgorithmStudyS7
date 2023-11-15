import copy

R, C = map(int, input().split())
islands = [list(input()) for _ in range(R)]
result = copy.deepcopy(islands)

for x in range(R):
    for y in range(C):
        if islands[x][y] == 'X':
            cnt = 0
            checks = [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]
            for check in checks:
                if -1 in check or check[0] == R or check[1] == C:
                    cnt += 1
                else:
                    if islands[check[0]][check[1]] == '.':
                        cnt += 1
            if cnt >= 3:
                result[x][y] = '.'

r1 = 0
r2 = R-1
c1 = 0
c2 = C-1

for r in range(R):
    if 'X' not in result[r]:
        r1 += 1
    else:
        break

for r in range(R-1, -1, -1):
    if 'X' not in result[r]:
        r2 -= 1
    else:
        break

result = result[r1:r2+1]

for c in range(C):
    if 'X' not in [r[c] for r in result]:
        c1 += 1
    else:
        break

for c in range(C-1, -1, -1):
    if 'X' not in [r[c] for r in result]:
        c2 -= 1
    else:
        break

result = [r[c1:c2+1] for r in result]

for r in result:
    print(''.join(r))

# 시간: 60ms