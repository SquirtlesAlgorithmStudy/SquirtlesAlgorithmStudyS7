

N = int(input())
houses = list(map(int, input().split()))
houses.sort()
if len(houses)%2==0:
    print(houses[(N//2)-1])
elif len(houses)%2==1:
    print(houses[N//2])
    
