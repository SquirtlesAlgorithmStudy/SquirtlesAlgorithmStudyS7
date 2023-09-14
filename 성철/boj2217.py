# 어떤 로프의 버틸수 있는 최대 중량이 k일때 리스트에서 k보다 큰 로프의 갯수를 구해야함

import sys
input = sys.stdin.readline

N = int(input())

rope = [int(input()) for _ in range(N)]
answer = 0
# 로프를 길이순으로 정렬
rope.sort()

# 길이순으로 정렬된 로프에서
for i in range(N):
    # 현재 로프 길이와 같거나 긴 로프의 갯수를 구해서 곱해줌
    cur = rope[i] * (N-i)
    # 그 값이 기존 최댓값보다 더 크면 교체
    if answer < cur:
        answer = cur

print(answer)