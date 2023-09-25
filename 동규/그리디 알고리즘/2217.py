N = int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr.sort()
count=0
result=max(arr)
chada=1

for i in range(2,max(arr)):
    count=0
    for j in arr:
        if j%i!=0:
            break
        elif j%i==0:
            count+=1
    if count==len(arr):
        chada=i
        break

for j in range(max(arr),10001,chada):
    count=0

    for i in range(1,N+1):
        if j/i<=min(arr[-i:]):
            break
        elif j/i>min(arr[-i:]):
            count+=1
    if count==N:
        result=j-chada
        break
print(result)