import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

# 나무 정렬
trees.sort()

start = 0
end = max(trees)
cut = 0

ans = 0
# 이분탐색
while start <= end:
    cut = (start + end) // 2

    # 잘린 나무 길이 총합
    total = 0
    for tree in trees:
        if tree > cut:
            total += tree - cut
    
    # 이분 탐색
    if total < m:
        end = cut - 1
    else:
        ans = cut
        start = cut + 1

print(ans)