import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))
# 오름차순으로 정렬
houses.sort()

# 중앙값
print(houses[(n-1)//2])