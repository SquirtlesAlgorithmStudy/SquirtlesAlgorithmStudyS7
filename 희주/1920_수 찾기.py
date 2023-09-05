import sys

result =[]
N = int(input())
N_list_set = set(list(map(int, sys.stdin.readline().split())))

M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))
M_list_set = set(M_list)

result =N_list_set & M_list_set

for i in range(M):
    if M_list[i] in N_list_set:
        print(1)
    else:
        print(0)

