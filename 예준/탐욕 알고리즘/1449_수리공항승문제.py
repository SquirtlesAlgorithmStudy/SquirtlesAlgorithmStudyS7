n, length = map(int, input().split())
location = list(map(float,input().split()))
location.sort()

tapes=0
check=0

for i in range(n):
    if(location[i]+0.5>check):
        tapes+=1
        check=location[i]+length-0.5
            
print(tapes)
