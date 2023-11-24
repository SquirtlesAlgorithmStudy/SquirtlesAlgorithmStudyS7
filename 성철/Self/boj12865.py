## BOJ 12865 : 평범한 배낭
## Gold 5
## Knapsack algorithm, dynamic programming

# N개의 물건, 각각 무게 W, 가치 V
# 최대 K만큼의 무게를 넣을 수 있는 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

# knapsack 알고리즘
# x축 : 1~K까지 가방의 무게(j) 최대 한도가 1인 가방부터 K인 가방까지 K개가 있다고 생각
# y축 : 물건 갯수 N개(i)


for i in range(1, N+1):
    for j in range(1, K+1):
        # 물건의 무게와 가치
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            # 가방에 담을 수 없음(배낭의 최대 수용 무게가 현재 물건의 무게보다 큼)
            knapsack[i][j] = knapsack[i-1][j] # 현재 물건을 넣을 수 없으므로 이전과 같은값을 가짐
        else:
            knapsack[i][j] = max(knapsack[i-1][j], value+knapsack[i-1][j-weight])
            # 넣지 않는 경우와 넣는 경우를 비교
            # 넣는 경우는 물건은 하나 덜넣고, 가방의 한도는 j-weight인 경우에 현재 물건을 넣음
            


