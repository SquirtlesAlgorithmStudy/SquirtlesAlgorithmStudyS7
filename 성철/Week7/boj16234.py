# NxN 크기의 땅
# 각각의 땅 = 하나의 나라
# graph[r][c]의 인구수 = A[r][c]
# 인접한 나라 사이 = 국경선

# 오늘부터 인구이동시작
# 더이상 인구이동이 없을 때 까지 진행

## 국경선을 공유하는 두 나라의 인구수 차이가 L 이상 R 이하면 하루동안 open
## 열린 칸을 통해 이동할 수 있으면(하나의 영역이 되면) 연합
## 연합을 이루고 있는 각 칸의 인구수 = 연합의 총 인구수 / 연합을 이루고 있는 칸의 갯수(소숫점 버림)
## 국경선 닫음

## 인구 이동이 며칠동안 이뤄지는지 출력

import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())

population = []

for _ in range(N):
    A = list(map(int, input().split()))
    population.append(A)





