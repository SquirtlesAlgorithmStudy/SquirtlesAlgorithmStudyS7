import sys
import math
n = int(input())
house_location = list(map(int,input().split()))

mean_loc= math.ceil(n/2)
house_location.sort()

print(house_location[mean_loc-1])