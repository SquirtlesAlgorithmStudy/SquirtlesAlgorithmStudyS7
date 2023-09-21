# 직관적으로 중간값에 배치했을때 가장 작을것이다

N = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()
print(arr[(N-1)//2])

