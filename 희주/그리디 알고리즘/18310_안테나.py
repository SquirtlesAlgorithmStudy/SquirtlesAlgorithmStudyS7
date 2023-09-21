import sys
# import heapq

N = int(input())
L = list(map(int,sys.stdin.readline().split()))
# result =[]
L.sort(reverse=False) # 집의 위치 오름차순 정렬

# curr = int(len(L)/2) # 중앙 인덱스 
# heapq.heappush(result, [sum([abs(l-L[curr]) for l in L]), L[curr]]) # 중앙에서의 거리 합
# heapq.heappush(result, [sum([abs(l-L[curr-1]) for l in L]), L[curr-1]]) # 집의 갯수가 짝수일 경우 더 작은 인덱스 위치 찾기 위해

# sum_length, i = heapq.heappop(result)

# print(i)
# # 집 위치 인덱스의 중앙에서부터의 거리 합이 최소이다.

print(L[(N-1)//2]) # 다른 사람 풀이.. 간단