# 18310 안테나          

n = int(input())
house = list(map(int, input().split()))

house.sort()

index = int(n/2 + n%2)

print(house[index-1])