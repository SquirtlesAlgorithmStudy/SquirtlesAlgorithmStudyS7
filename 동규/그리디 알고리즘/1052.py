import sys

N, K = map(int,sys.stdin.readline().split())

bottle_count=0
liter=1

while True:
    if N%2!=0:
        N+=1
        bottle_count+=liter
        print(liter)        
    elif N%2==0:
        N//=2
        liter*=2
        print("N",N,"liter",liter)
    if N<=K:
        break

print(bottle_count)