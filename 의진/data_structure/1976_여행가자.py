import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
dis_mat = [list(map(int, input().split())) for _ in range(N)]
path = list(map(int, input().split()))

parent = [i for i in range(N+1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)

    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root


for i in range(N):
    for j in range(i + 1, N):
        if dis_mat[i][j] == 1:
            union_parent(parent, i+1, j+1)

prev_root = find_parent(parent, path[0])
is_possible = True
for item in path[1:]:
    if prev_root != find_parent(parent, item):
        is_possible = False
        break
print("YES") if is_possible else print("NO")
