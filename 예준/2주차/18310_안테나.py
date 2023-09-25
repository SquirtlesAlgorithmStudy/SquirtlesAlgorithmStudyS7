import sys
import math
n = int(input())
house_location = list(map(int,input().split()))

mean_loc= math.ceil(n/2) # 전체 개수의 중간 위치 + 1 값
house_location.sort() # 정렬

print(house_location[mean_loc-1])